#!/usr/bin/python3
"""Creates a Square Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Private instance attribute size
    Public method area()
    Inherits from Rectangle
    """

    def __init__(self, size):
        """Initializes a Square
        Args:
            size: size of the square
        """

        self.integer_validation("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """gets area"""

        return self.__size ** 2
