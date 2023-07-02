#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL.
Usage: ./7-error_code.py <URL>
  - Also handles HTTP errors.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
