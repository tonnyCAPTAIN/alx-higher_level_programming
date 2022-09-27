#!/usr/bin/python3
"""function that writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a str i.e text to filename"""

    with open(filename, 'w') as f:
        return f.write(text)
