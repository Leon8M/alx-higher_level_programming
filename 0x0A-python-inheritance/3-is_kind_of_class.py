#!/usr/bin/python3
"""
Module containing is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    :param obj: object to test
    :param a_class: class to test over
    :return: True or false on each case
    """
    return isinstance(obj, a_class)
