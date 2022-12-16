#!/usr/bin/python3
"""initialize"""
import requests
from sys import argv


def get_commits():
    """display commits and author"""
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    req = requests.get(url)
    json = req.json()

    try:
        for i in range(0, 10):
            sha = json[i].get('sha')
            author = json[i].get('commit').get('author').get('name')
            print('{}: {}'.format(sha, author))
    except IndexError:
        pass


if __name__ == '__main__':
    get_commits()
