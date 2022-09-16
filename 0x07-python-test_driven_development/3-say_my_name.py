#!/usr/bin/python3
"""
returning first name and last name
Args:
    first name
    lastname = default toempty string
"""

def say_my_name(first_name, last_name=""):
    """ Prints "My name is <first name> <last name>"
    checks if both fist name and last nme are strings
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
