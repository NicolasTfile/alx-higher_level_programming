#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter.
Usage: ./6-post_email.py <URL> <email>
  - Also displays the body of the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    email_val = {"email": argv[2]}

    response = requests.post(url, data=email_val)
    print(response.text)
