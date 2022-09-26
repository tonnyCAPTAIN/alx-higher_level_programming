#!/usr/bin/python3
"""Creates a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Private instances attributes:
    -width - heigth
    Public method area()
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """initialize instances
        Args:
            width: rectangle width
            height: rectangle height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """gets the area"""

        return self.__width * self.__height
