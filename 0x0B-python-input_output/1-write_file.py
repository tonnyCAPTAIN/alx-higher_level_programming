#!/usr/bin/python3
"""function that writes a string to a text file
and returns the number of characters written
"""


def number_of_lines(filename=""):
    """function returning number of characters
    in filename
    """

    counter = 0
    with open(filename, encoding="utf-8") as f:
        text = f.readlines()
        for line in text:
            counter += 1

    return counter
