#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response (decoded in utf-8).
Usage: ./3-error_code.py <URL>
  - Also handles HTTP errors.
"""
import sys
import urllib


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
