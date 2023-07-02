#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    body = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))
