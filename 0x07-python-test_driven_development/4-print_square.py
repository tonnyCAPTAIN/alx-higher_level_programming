#!/usr/bin/python3

"""Printing a square with #
Args:
    size- should be integer above 0 only
"""
def print_square(size):
    """print square with #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
