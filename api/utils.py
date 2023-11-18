import logging
import os
from urllib.parse import urlparse, parse_qs

import requests
from requests import Response

FILMS_BASE = "https://ghibli.rest/films"


def get_ghibli_films():
    logging.info("Fetching data from Ghibli APIs")
    films_response: Response = requests.get(FILMS_BASE)
    films: list = films_response.json()

    if os.environ.get("ENV", "DEV") == "TEST":
        logging.info("====> Running tests")
        logging.info("====> Reducing number of films being used to 5")
        films = films[:5]

    logging.info("Fetched all films")

    people_url_set: set = set()

    # one person could be part of multiple films
    # here we create a set of person urls to reduce the number of calls to the person api
    for film in films:
        people_url_set.update(film["people"])

    logging.info("Fetching people data")
    # query the person api and create a map of person url and person details
    people_map: dict = {}
    for person_url in people_url_set:
        parsed_person_url = urlparse(person_url)
        query_string_map = parse_qs(parsed_person_url.query, keep_blank_values=True)
        # to ensure we don't query the person endpoint without any ids
        if len(list(filter(lambda x: x != "", query_string_map.get("id")))) > 0:
            person_response = requests.get(person_url)
            person = person_response.json()
            people_map[person_url] = person[0]

    logging.info("Preparing API response")
    for film in films:
        actors = []
        for person_url in film["people"]:
            actor = people_map.get(person_url, None)
            if actor is not None:
                actors.append(
                    {
                        "id": actor["id"],
                        "name": actor["name"],
                        "species": actor["species"],
                        "url": actor["url"],
                    }
                )

        film["actors"] = actors

        film.pop("people", None)

    return films
