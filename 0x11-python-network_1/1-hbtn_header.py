#!/usr/bin/python3
"""Fetches the header"""
import urllib.request
import sys


def fetcher():
    """fetches the header"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header["X-Request-Id"])


if __name__ == "__main__":
    fetcher()
