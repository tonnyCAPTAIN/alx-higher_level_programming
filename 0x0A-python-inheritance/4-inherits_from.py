#!/usr/bin/python3
"""if the object is an instance of a class that inherited
(directly/indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Determines if obj is an instance of a class that
    inherited from a_class

    Args:
        obj
        a_class
    """

    return isinstance(obj, a_class) and type(obj) != a_class
