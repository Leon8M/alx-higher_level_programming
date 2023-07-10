#!/usr/bin/python3
"""
Module containing BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Raises Exception
        :return: Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        :param name: name
        :param value: value
        :return: nothing
        :raises: TypeError if value is not int
                 ValueError if value less or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
