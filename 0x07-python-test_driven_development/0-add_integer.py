#!/usr/bin/python3
"""
Module with add_integer function
"""


def add_integer(a, b=98):
    """
    Adds two integers, a and b
    Args:
        a (int or float): first number
        b (int or float): second number (default is 98)
    :return: int: sum of a and b
    :raises: TypeError: If `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
