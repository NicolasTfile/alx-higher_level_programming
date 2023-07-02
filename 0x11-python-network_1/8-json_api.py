#!/usr/bin/python3
"""Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
Usage: ./8-json_api.py <letter>
"""
from sys import argv
import requests


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    value = {"q": letter}

    req = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
