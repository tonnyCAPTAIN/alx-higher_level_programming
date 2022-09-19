#!/usr/bin/python3
"""Rectangle with height and width"""


class Rectangle:
    """ Rectangle data i.e height and width"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instantiating"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns whichever is bigger, rect_1 or rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a square of the size"""
        height = size
        width = size
        return cls(height, width)

    def __str__(self):
        """print() __str__ method funtion to return rectangle in char '#'
        """
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res

        for i in range(self.__height):
            for i2 in range(self.__width):
                res += str(self.print_symbol)
            if i != self.__height - 1:
                res += '\n'
        return res

    def __repr__(self):
        """print() or eval() __repr__ method function to return
        ... Rectangle(width, height)
        """
        w = str(self.__width)
        h = str(self.__height)

        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        """Print a message for del
        decrement instance when del is called
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

