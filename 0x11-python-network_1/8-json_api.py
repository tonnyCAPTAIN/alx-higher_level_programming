#!/usr/bin/python3
"""initialize"""
import requests
from sys import argv


def post_q():
    """post a variable"""
    try:
        q = argv[1]
    except IndexError:
        q = ''

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    req = requests.post(url, data)
    try:
        j_format = req.json()
        if (len(j_format) == 0):
            print('No result')
        else:
            id_no = j_format.get('id')
            name = j_format.get('name')
            print('[{}] {}'.format(id_no, name))
    except ValueError:
        print('Not a valid JSON')


if __name__ == '__main__':
    post_q()
