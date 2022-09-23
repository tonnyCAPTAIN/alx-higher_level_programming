#!/usr/bin/python3

"""Printing a square with #
Args:
    size- should be integer above 0 only
"""


def print_square(size):
    """This function prints a square with the character #
    Args:
        size (int): This represents the length of the square
    """
    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
