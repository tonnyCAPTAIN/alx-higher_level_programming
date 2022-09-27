#!/usr/bin/python3
"""Reads a file and prints output"""


def read_file(filename=""):
    """takes filename and prints its
    contents to the stdout
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
