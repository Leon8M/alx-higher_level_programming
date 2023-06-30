#!/usr/bin/python3
"""
Module with matrix_divided function
"""


def print_square(size):
    """
    Prints a square of a provided length.
    :param size: length provided.
    :return: nothing.
    :raises: TypeError if size is not an integer.
             TypeError if size is a float and less than 0.
             ValueError if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
