#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """public instance methods are and integer validator"""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validataes the value passed"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
