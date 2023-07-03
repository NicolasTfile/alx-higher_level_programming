#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user.
Usage: ./8-json_api.py <letter>"""

import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    val = {"q": letter}

    response = requests.post(url, data=val)

    try:
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
