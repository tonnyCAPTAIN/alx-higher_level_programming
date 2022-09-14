#!/usr/bin/python3
"""creating a class"""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new square.
        Args:
        size (int): The size of the squre
        position (int, int): The position of the new sqaure
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """current square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """ printing the sqaure"""
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print('')
        if self.__size == 0:
            print("")
