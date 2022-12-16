#!/usr/bin/python3
"""initialize"""
import requests
from sys import argv


def post_email():
    """post an email"""
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)


if __name__ == '__main__':
    post_email()
