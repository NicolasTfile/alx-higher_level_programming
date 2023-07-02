#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter. Displays the body of the response (decoded in utf-8).
Usage: ./2-post_email.py <URL> <email>
"""


from sys import argv
from urllib.parse import urlencode
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")

    req = Request(url, data)
    with urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
