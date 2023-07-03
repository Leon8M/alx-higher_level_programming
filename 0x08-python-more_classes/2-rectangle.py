#!/usr/bin/python3
"""Module containing Rectangle  class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Get width and height
        :param width: width
        :param height: height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width
        :return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width to value
        :param value: value
        :return: width to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height
        :return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height to value
        :param value: Value
        :return: height to value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area
        :return: area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Perimeter
        :return: perimeter
        """
        return 2 * (self.width + self.height)
