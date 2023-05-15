def verify_gare(gare, gares):
    if gare not in gares:
        raise ValueError(
            "La gare " + gare + " n'existe pas, essayez --list-gares pour avoir la liste des gares disponibles")


def verify_argument(depart, arrivee, date, steps, gares):
    if depart == arrivee:
        raise ValueError(
            "La gare d'arrivée doit être différente de la gare de départ")
    if steps < 1:
        raise ValueError("Le nombre d'étape doit être supérieur ou égal à 1")
    verify_gare(depart, gares)
    verify_gare(arrivee, gares)


def formalize_gare(gare):
    gare = gare.replace(" ", "+")
    return gare
