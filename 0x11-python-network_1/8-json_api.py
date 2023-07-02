#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
Usage: ./8-json_api.py <letter>"""

import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}

    response = requests.post(url, data=payload)

    try:
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
