#!/usr/bin/python3
"""Takes GitHub credentials (username and password) and uses the GitHub API to display id.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    body = response.json()
    print(body.get("id"))
