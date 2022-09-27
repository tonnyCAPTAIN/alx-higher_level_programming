#!/usr/bin/python3
"""returns python objects from json"""

import json


def from_json_string(my_str):
    """function reryurning python objects"""

    return json.loads(my_str)
