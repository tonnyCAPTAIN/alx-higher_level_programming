#!/usr/bin/python3
"""getting list of available attributes & methods of an object"""


def lookup(obj):
    """Returns that list of attributes and methods
    Args: obj: object to check
    """

    return dir(obj)
