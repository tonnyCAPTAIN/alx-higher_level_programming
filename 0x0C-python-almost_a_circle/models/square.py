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

        update = ("id", "size", "x", "y")
        length = len(args)
        if args:
            for i in range(length):
                setattr(self, update[i], args[i])
        elif not args or update < 1:
            for key, value in kwargs.items():
                if key in update:
                    setattr(self, key, value)

        def to_dictionary(self):
            """dictionary square represetation"""

            return {
                    'id': self.id,
                    'x': self.x,
                    'size': self.width,
                    'y': self.y
                    }
