from urllib3 import request


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
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    url = (
        "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=1000"
        + "&sort=-date&facet=date&facet=origine&facet=destination&facet=od_happy_card&refine.origine="
        + depart
        + "&refine.od_happy_card=OUI&refine.date="
        + date
        + "&refine.destination="
        + arrivee
    )
    response = request("GET", url)
    return parse_api_answer(eval(response.data), hour)


def check_available_gares(depart, date, hour):
    gares = []
    url = (
        "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=1000"
        + "&sort=-date&facet=date&facet=origine&facet=destination&facet=od_happy_card&refine.origine="
        + depart
        + "&refine.od_happy_card=OUI&refine.date="
        + date
    )

    response = request("GET", url)

    return parse_api_answer(eval(response.data), hour)
