#!/usr/bin/python3
"""Takes GitHub credentials and uses the GitHub API to display id.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""

from sys import argv
import requests


def get_gh_id(username, password):
    """
    function for getting the Id
    Args: username and password
    """
    url = "https://api.github.com/user"
    auth = (username, password)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('id')
    else:
        return None


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    user_id = get_gh_id(username, password)
    print(user_id)
