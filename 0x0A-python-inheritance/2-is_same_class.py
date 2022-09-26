#!/usr/bin/python3
"""if an object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """function determines if obj is an instance of a_class
    Args:
        obj: object to look at
        a_class: class to verify the instanceof

    Returns: True if obj is an instance of a_class othereise false
    """
    return True if type(obj) is a_class else False
