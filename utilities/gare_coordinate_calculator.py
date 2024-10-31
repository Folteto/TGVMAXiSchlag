import os
from geopy.distance import geodesic
import unicodedata

base_dir = os.path.dirname(os.path.abspath(__file__))
gares_txt_path = os.path.join(base_dir, "..", "data", "gares_coordinates.txt")
gps_txt_path = os.path.join(base_dir, "..", "data", "liste-des-gares.csv")


def get_gares_from_file(file):
    gares = []
    with open(file, "r") as f:
        for line in f:
            gares.append(line.strip())
    return gares


def parse_liste_des_gares_coord(csv):
    gares_dict = {}
    with open(gps_txt_path, "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            values = line.split(";")
            gare_name = values[1]
            coordinates = (
                values[-1]
                .strip('"{}')
                .split(":")[1]
                .replace("[", "")
                .replace("]", "")
                .split(",")[:-1]
            )
            gares_dict[gare_name] = {
                "latitude": float(coordinates[1]),
                "longitude": float(coordinates[0]),
            }
    return gares_dict


def normalize_gare_name(nom_gare):
    # Supprimer les accents
    nom_sans_accent = "".join(
        (
            c
            for c in unicodedata.normalize("NFD", nom_gare)
            if unicodedata.category(c) != "Mn"
        )
    )
    # Mettre en majuscules et supprimer les espaces
    nom_normalise = nom_sans_accent.upper().replace(" ", "").replace("-", "")
    return nom_normalise


def calculate_distance_matrix(gares_dict):
    gares_list = list(gares_dict.keys())
    matrix = []
    for gare1 in gares_list:
        row = []
        coord1 = (gares_dict[gare1]["latitude"], gares_dict[gare1]["longitude"])
        for gare2 in gares_list:
            coord2 = (gares_dict[gare2]["latitude"], gares_dict[gare2]["longitude"])
            distance = geodesic(coord1, coord2).kilometers
            row.append(distance)
        matrix.append(row)
    return matrix


gares_tgvmax = get_gares_from_file(gares_txt_path)

gares_dict_full = parse_liste_des_gares_coord("..\data\liste-des-gares.csv")
list_normalized_full = [normalize_gare_name(g) for g in gares_dict_full.keys()]

for g in gares_tgvmax:
    if normalize_gare_name(g) not in list_normalized_full:
        print(g + "---" + normalize_gare_name(g))

print("\n-------")
# print(list_normalized_full)

##to do : ajouter les gares intramuros dans liste-des-gares.csv et les coordonnées manquantes
## créer un nouveau dictionnaire des gares tgv max avec les coordonnées et si les coordonnées sont manquantes, mettre 0 et 0
## Compute la distance matrix avec les gares tgv max via le dcitionnaire des gares tgv max précédemment créé
