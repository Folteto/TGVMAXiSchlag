import argparse
import requests


from utilities import argument_check, api_requests, recursive_checker


parser = argparse.ArgumentParser(
    prog="TGVMAXiSchlag",
    description="Find the best TGVmax route for your trip, regardless where you have to stop",
)
parser.add_argument("-d", "--depart", help="Departure station", required=True)
parser.add_argument("-a", "--arrivee", help="Arrival station", required=True)
parser.add_argument("-t", "--date", help="Date of the trip", required=True)
parser.add_argument(
    "-s", "--steps", help="Number of max steps, default 2", required=False, default=2
)
parser.add_argument(
    "-l",
    "--list-gares",
    help="List all available stations",
    required=False,
    action="store_true",
)
parser.add_argument(
    "-p",
    "--propale",
    help="List TGVmax trains from your station at your desired date",
    required=False,
    action="store_true",
)
parser.add_argument(
    "-f",
    "--force",
    help="L'algorithme recherche des trajets avec le nombre minimum d'étapes possibles. Cette option active le forçage de la recherche de trajets jusqu'au nombre d'étapes indiqué.",
    required=False,
    action="store_true",
)
args = parser.parse_args()

depart = args.depart
arrivee = args.arrivee
date = args.date
force_maxsteps = args.force
steps = int(args.steps)

# Corps
print("\n\n")
print(
    " /$$$$$$$$ /$$$$$$  /$$    /$$ /$$      /$$  /$$$$$$  /$$   /$$ /$$  /$$$$$$            /$$       /$$"
)
print(
    "|__  $$__//$$__  $$| $$   | $$| $$$    /$$$ /$$__  $$| $$  / $$|__/ /$$__  $$          | $$      | $$"
)
print(
    "   | $$  | $$  \__/| $$   | $$| $$$$  /$$$$| $$  \ $$|  $$/ $$/ /$$| $$  \__/  /$$$$$$$| $$$$$$$ | $$  /$$$$$$   /$$$$$$"
)
print(
    "   | $$  | $$ /$$$$|  $$ / $$/| $$ $$/$$ $$| $$$$$$$$ \  $$$$/ | $$|  $$$$$$  /$$_____/| $$__  $$| $$ |____  $$ /$$__  $$"
)
print(
    "   | $$  | $$|_  $$ \  $$ $$/ | $$  $$$| $$| $$__  $$  >$$  $$ | $$ \____  $$| $$      | $$  \ $$| $$  /$$$$$$$| $$  \ $$"
)
print(
    "   | $$  | $$  \ $$  \  $$$/  | $$\  $ | $$| $$  | $$ /$$/\  $$| $$ /$$  \ $$| $$      | $$  | $$| $$ /$$__  $$| $$  | $$"
)
print(
    "   | $$  |  $$$$$$/   \  $/   | $$ \/  | $$| $$  | $$| $$  \ $$| $$|  $$$$$$/|  $$$$$$$| $$  | $$| $$|  $$$$$$$|  $$$$$$$"
)
print(
    "   |__/   \______/     \_/    |__/     |__/|__/  |__/|__/  |__/|__/ \______/  \_______/|__/  |__/|__/ \_______/ \____  $$"
)
print(
    "                                                                                                                /$$  \ $$"
)
print(
    "                                                                                                               |  $$$$$$/"
)
print(
    "                                                                                                                \______/ "
)

# import des gares depuis le fichier txt

with open("data\gares.txt", "r") as f:
    gares = f.readlines()
    gares = [gare.strip() for gare in gares]
    gares.sort()

if args.list_gares:
    print("Liste des gares disponibles :")
    for gare in gares:
        print(gare)
    exit()

if args.propale:
    print("Trains TGVmax disponibles depuis " + depart + " le " + date)
    trains = api_requests.check_available_gares(
        argument_check.formalize_gare(depart), date
    )
    for train in trains:
        print("Vers la gare de " + train[1])
        print("Heure de départ : " + train[2] + " Heure d'arrivée : " + train[3])
    exit()

# vérification des arguments et formalisation des gares

argument_check.verify_argument(depart, arrivee, date, steps, gares)
depart_req = argument_check.formalize_gare(depart)
arrivee_req = argument_check.formalize_gare(arrivee)

# on commence par vérifier qu'il n'existe pas de trajet direct entre les deux gares

available_trains = api_requests.simple_request(depart_req, arrivee_req, date)

if len(available_trains) > 0:
    print(
        "Il existe au moins un trajet direct entre "
        + depart
        + " et "
        + arrivee
        + " le "
        + date
    )
    print("Voici les trains disponibles :")
    for train in available_trains:
        print("Heure de départ : " + train[2] + " Heure d'arrivée : " + train[3])
else:
    print(
        "Il n'existe pas de trajet direct entre "
        + depart
        + " et "
        + arrivee
        + " le "
        + date
    )

print("")
print("Recherche de trajets avec étapes...")
print("")


print("Tentative de trouver des trajets avec ", steps, " étapes...")

all_compatible_journey = []
recursive_checker.gare_checker(
    all_compatible_journey, arrivee, depart, date, [], steps, force_maxsteps
)

if len(all_compatible_journey) > 0:
    print("Trajet trouvé ! Voici les trains à prendre :")
    for trajet in all_compatible_journey:
        print("Trajet :")
        for i in range(len(trajet)):
            train = trajet[i]
            print("Train ", i + 1)
            print(
                "Départ de ",
                train[0],
                " à ",
                train[2],
                " ---> Arrivée à ",
                train[1],
                " à ",
                train[3],
            )
        print("------------------")
else:
    print("Aucun train trouvé, essayez une profondeur plus élevée !")
