#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if (value <= 0):
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif (value <= 0):
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif (value < 0):
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif (value < 0):
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.height * self.width

    def display(self):
        """Print the Rectangle using the `#` character."""
        if (self.width == 0) or (self.height == 0):
            print()
            return

        [print() for y in range(0, self.y)]
        for h in range(0, self.height):
            [print(" ", end="") for x in range(0, self.x)]
            [print("#", end="") for w in range(0, self.width)]
            print()

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, a in enumerate(args):
                # enumerate gives both the index and value respectively
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return ({"id": self.id, "width": self.width,
                 "height": self.height, "x": self.x,
                 "y": self.y})
