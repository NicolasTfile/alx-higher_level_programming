#!/usr/bin/python3
"""List 10 commits of the repository by the user.
Usage: ./100-github_commits.py <repo name> <repo owner>
"""

from sys import argv
import requests


def commit_list(repo, owner):
    """
    function for getting the list of commits
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repository = argv[1]
    owner = argv[2]
    commit_list(repo, owner)
