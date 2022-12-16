#!/usr/bin/python3
"""initialize"""
import requests
from sys import argv


def request_status():
    """request status code"""
    req = requests.get(argv[1])
    code = req.status_code

    if(code == 200):
        print(req.text)
    else:
        print('Error code: {}'.format(req.status_code))


if __name__ == '__main__':
    request_status()
