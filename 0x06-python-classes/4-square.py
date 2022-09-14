#!/usr/bin/python3
"""Creating a sqaure"""


class Square:
    """Define  a  Square class"""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square
            """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """setting the size of sqaure"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area of sqaure"""
        return (self.__size ** 2)
