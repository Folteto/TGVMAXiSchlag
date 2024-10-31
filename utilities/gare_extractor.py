import os
from geopy.distance import geodesic
import unicodedata


def import_gares_from_csv(csv):
    gares = []
    with open(csv, "r") as f:
        for line in f:
            gare = line.split(";")[6]
            if gare not in gares:
                gares.append(gare)
            gare2 = line.split(";")[7]
            if gare2 not in gares:
                gares.append(gare2)
    return gares


def write_gares_to_file(gares, file):
    with open(file, "w") as f:
        for gare in gares:
            f.write(gare + "\n")


base_dir = os.path.dirname(os.path.abspath(__file__))
tgvmax_csv_path = os.path.join(base_dir, "..", "data", "tgvmax.csv")
gares_txt_path = os.path.join(base_dir, "..", "data", "export_gare_tgvmax_raw.txt")

gares_tgvmax = import_gares_from_csv(tgvmax_csv_path)
write_gares_to_file(gares_tgvmax, gares_txt_path)
