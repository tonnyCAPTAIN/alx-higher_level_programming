#!/usr/bin/python3
"""initialize"""
import requests
from sys import argv


def get_githubId():
    """display Github id"""
    req = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    json = req.json()
    github_id = json.get('id')
    print(github_id)


if __name__ == '__main__':
    get_githubId()
