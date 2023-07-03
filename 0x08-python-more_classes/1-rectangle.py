#!/usr/bin/python3
"""Module containing Rectangle  class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Takes width and height of rectangle
        :param width: width
        :param height: height
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        Sets height
        :return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height.
        :param value: value to view
        :return: height equal to value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Sets the width
        :return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width
        :param value: value to view
        :return: width with respect to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
