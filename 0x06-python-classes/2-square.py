#!/usr/bin/python3
""" define a class squre"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:

        size (int): The size of the new square
        """

        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
