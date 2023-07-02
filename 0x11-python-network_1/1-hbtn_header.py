#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable found in the header of the response.
Usage: ./1-hbtn_header.py <URL>
"""
from sys import argv
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = argv[1]

    req = Request(url)
    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
