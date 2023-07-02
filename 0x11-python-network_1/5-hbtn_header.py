#!/usr/bin/python3
"""Displays the value of the variable X-Request-Id in the response header.
Usage: ./5-hbtn_header.py <URL>
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
