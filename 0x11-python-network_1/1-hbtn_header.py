#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable found in the header of the response.
Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        req_id = response.headers['X-Request-Id']
        print(req_id)
