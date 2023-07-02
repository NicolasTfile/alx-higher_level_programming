#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response (decoded in utf-8).
Usage: ./3-error_code.py <URL>
  - Also handles HTTP errors.
"""
from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = argv[1]

    req = Request(url)
    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
