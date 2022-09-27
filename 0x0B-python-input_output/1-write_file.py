#!/usr/bin/python3
"""function that writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """text given to be written in
    filename
    """

    with open(filename, 'W', encoding="utf-8") as f:
        f = f.write(text)
        j = f.readline()
        return (j)
