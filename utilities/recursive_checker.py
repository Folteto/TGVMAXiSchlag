from . import argument_check, api_requests


def gare_checker_unique(global_tableau, arrivee, depart, date, trajet, profondeur):
    if len(trajet) == 0:
        depart_req = argument_check.formalize_gare(depart)
        available_gares = api_requests.check_available_gares(depart_req, date)
        for gare in available_gares:
            gare_checker_unique(
                global_tableau, arrivee, depart, date, [gare], profondeur
            )

    elif len(trajet) <= profondeur:
        depart_req = argument_check.formalize_gare(
            trajet[-1][1]
        )  # le dernier train du trajet a pour destination la prochaine origine
        heure_depart_min = trajet[-1][3]  # idem avec l'heure d'arrivée
        available_gares = api_requests.check_available_gares(depart_req, date)
        for gare in available_gares:
            if gare[3] > gare[2] and gare[2] > heure_depart_min:
                newtrajet = trajet.copy()
                newtrajet.append(gare)
                if gare[1] == arrivee:
                    global_tableau.append(newtrajet)
                    print("J'ai trouvé un trajet gros bg")
                    for garee in newtrajet:
                        print(
                            "Départ de ",
                            garee[0],
                            " à ",
                            garee[2],
                            " ---> Arrivée à ",
                            garee[1],
                            " à ",
                            garee[3],
                        )
                    print("------------------")
                else:
                    gare_checker_unique(
                        global_tableau, arrivee, depart, date, newtrajet, profondeur
                    )
    else:
        return None


def gare_checker(global_tableau, arrivee, depart, date, trajet, profondeur, force):
    if force:
        gare_checker_unique(global_tableau, arrivee, depart, date, trajet, profondeur)
    else:
        prof = 1
        while len(global_tableau) == 0 and prof <= profondeur:
            gare_checker_unique(global_tableau, arrivee, depart, date, trajet, prof)
            prof += 1
