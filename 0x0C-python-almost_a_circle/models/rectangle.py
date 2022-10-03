#!/usr/bin/python3
"""REctangle class"""


from models.base import Base


class Rectangle(Base):
    """Creating Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init Rectangle method"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getting width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setting width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getting height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setting height value"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getting x"""

        return self.__x

    @x.setter
    def x(self, value):
        """setting x value"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getting y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setting y value"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return rectangle area"""

        return (self.__width * self.__height)

    def display(self):
        """print a rectangle with #"""

        for y_space in range(self.__y):
            print()
        for column in range(self.__height):
            for x_space in range(self.__x):
                print(" ", end='')
            for row in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """display formated info"""

        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """update Rectangle"""

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """returning rectangle in dict"""

        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}