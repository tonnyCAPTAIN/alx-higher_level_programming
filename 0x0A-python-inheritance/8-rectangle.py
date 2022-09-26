#!/usr/bin/python3
"""Creates a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with private instance attribute
    that inherits from basegeometry class
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
