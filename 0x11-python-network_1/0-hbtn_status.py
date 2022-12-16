#!/usr/bin/python3
"""fetch url with urlib"""
from urllib.request import urlopen


def status():
    """fetch url body"""
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        convert = body.decode('utf-8')
        print('Body response:\n\t- type: {}'.format(type(body)))
        print('\t- content: {}\n\t- utf8 content: {}'.
              format(body, convert, end=''))


if __name__ == '__main__':
    status()
