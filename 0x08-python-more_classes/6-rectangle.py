#!/usr/bin/python3
"""Rectangle with height and width"""


class Rectangle:
    """ Rectangle data i.e height and width"""
    def __init__(self, width=0, height=0):
        """instantiating"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returning width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """returning height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return area of rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """print() __str__ method funtion to return rectangle in char '#'"""
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res
        for i in range(self.__height):
            if i == self.__height - 1:
                res += ('#' * self.__width)
            else:
                res += (('#' * self.__width) + '\n')
        return res

    def __repr__(self):
        """print() or eval() __repr__ method function to return
        ..Rectangle(width, height)"""
        w = str(self.__width)
        h = str(self.__height)

        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        """Print a message for del
        Decrement instance when del is called
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
