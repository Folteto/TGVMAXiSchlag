## inutile pour le moment


def date_precedente(date):
    annee, mois, jour = date.split("-")
    if jour != "01":
        jour = str(int(jour) + 1)
    else:
        if mois in ["01", "03", "05", "07", "08", "10", "12"]:
            pass
