#!/usr/bin/python3
def add_integer(a, b=98):
    """ returns addition of a and b
    Args:
        a = 1st num
        b = 2nd num

    TypeError: If a or b aren't integer and/or float numbers
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b


