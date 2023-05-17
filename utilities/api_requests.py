import requests


def parse_api_answer(answer, hour):
    answer = answer["records"]
    trains = []
    for train in answer:
        train = train["fields"]
        train = [
            train["origine"],
            train["destination"],
            train["heure_depart"],
            train["heure_arrivee"],
        ]
        if train[2] >= hour:
            trains.append(train)
    return trains


def simple_request(depart, arrivee, date, hour):
    url = (
        "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=1000"
        + "&sort=-date&facet=date&facet=origine&facet=destination&facet=od_happy_card&refine.origine="
        + depart
        + "&refine.od_happy_card=OUI&refine.date="
        + date
        + "&refine.destination="
        + arrivee
    )

    response = requests.get(url)

    return parse_api_answer(eval(response.text), hour)


def check_available_gares(depart, date, hour):
    gares = []
    url = (
        "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=1000"
        + "&sort=-date&facet=date&facet=origine&facet=destination&facet=od_happy_card&refine.origine="
        + depart
        + "&refine.od_happy_card=OUI&refine.date="
        + date
    )

    response = requests.get(url)

    return parse_api_answer(eval(response.text), hour)
