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
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @property.setter
    def position(self, value):
        """
        setter for the position attribute
        Args:
            value: tuple of non negative int to be set to position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        getting area of a square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        prints the square with #
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.position[0] + "#" * self.__size
                for i in range(self.__size)]))
