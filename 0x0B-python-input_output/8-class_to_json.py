#!/usr/bin/python3
"""function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and
boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """module class_to_json
    returns builds a dictionary
    """

    return obj.__dict__
