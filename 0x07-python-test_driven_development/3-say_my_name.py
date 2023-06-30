#!/usr/bin/python3
"""
Module with matrix_divided function
"""


def say_my_name(first_name, last_name=""):
    """
    prints the first and last names provided.
    :param first_name: first name provided
    :param last_name: last name provided
    :return: nothing
    :raises: TypeError if  names are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
