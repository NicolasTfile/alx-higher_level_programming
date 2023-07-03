#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL.
Usage: ./2-post_email.py <URL> <email>
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = urlencode({'email': email}).encode('utf-8')
    with urlopen(url, data=data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
