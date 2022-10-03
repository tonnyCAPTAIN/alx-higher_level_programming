#!/usr/bin/python3
"""a class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherit
    from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of Square class
        Attributes:
            size is the size of the square
            x is space
            y sis spce
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        size.width = value
        size.height = value

    def __str__(self):
        """Returns string representation of Square """
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updating the square values"""

        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
            """dictionary square represetation"""

        return {
                'id': self.id,
                'x': self.x,
                'size': self.width,
                'y': self.y
                 }
