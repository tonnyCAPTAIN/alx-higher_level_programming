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
        return"[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

     

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the Squares's dict """
        s_dict = {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
        return s_dict
