#!/usr/bin/python3
"""DEfine a class Square"""


class Square:
    """
    class Square
    """
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square
            """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
  
    def area(self):
        """Find are of sqaure"""
        return(self.__size * self.__size)
