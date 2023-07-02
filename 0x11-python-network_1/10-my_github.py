#!/usr/bin/python3
"""Takes GitHub credentials (username and password) and uses the GitHub API to display id.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""

import sys
import requests


def get_github_id(username, password):
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
    username = sys.argv[1]
    password = sys.argv[2]
    user_id = get_github_id(username, password)
    print(user_id)
