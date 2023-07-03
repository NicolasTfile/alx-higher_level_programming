#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response.
Usage: ./3-error_code.py <URL>
  - Also handles HTTP errors.
"""
from urllib.request import urlopen
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except HTTPError as e:
        print("Error code:", e.code)
