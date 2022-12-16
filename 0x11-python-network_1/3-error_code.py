#!/usr/bin/python3
"""initialize"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


def errorCode():
    """post values to a url and get error code"""
    url = argv[1]

    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    errorCode()
