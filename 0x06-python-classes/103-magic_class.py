#!/usr/bin/python3
import math
"""
Module that contains the MagicClass class.
"""


class MagicClass:
    """
    A class representing a magic circle.

    Args:
        radius (float or int): The radius of the circle. Default is 0.

    Raises:
        TypeError: If radius is not a number (float or int).

    Attributes:
        __radius (float or int): The radius of the circle.

    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a given radius.

        Args:
            radius (float or int): The radius of the circle. Default is 0.

        Raises:
            TypeError: If radius is not a number (float or int).

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.

        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.

        """
        return 2 * math.pi * self.__radius
