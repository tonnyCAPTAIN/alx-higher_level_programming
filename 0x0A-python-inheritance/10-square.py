#!/usr/bin/python3
"""Creates a square class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Private instance attribute size
    Public method area()
    Inherits from Rectangle
    """

    def __init__(self, size):
        """initilize a square
        Args:
            - size:
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """gets area of a squre"""

        return self.__size ** 2
