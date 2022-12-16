#!/usr/bin/python3
"""initialize"""
import requests
from sys import argv


def extract_header():
    """extract header key X-Request_id"""
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))


if __name__ == '__main__':
    extract_header()
