#!/usr/bin/python3

"""Takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter. Displays the body of the response (decoded in utf-8).
Usage: ./2-post_email.py <URL> <email>
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
