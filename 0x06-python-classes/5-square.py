#!/usr/bin/python3
"""Creating a class"""


class Square:
    """ Square class"""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
        size (int): The size of the new squa
        """
        self.__size = size

    @property
    def size(self):
        """ Getting the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        def area(self):
            """area of the square """
            return (self.__size ** 2)

        def my_print(self):
            """ printing the sqaure"""
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
            if self.__size == 0:
                print("")
