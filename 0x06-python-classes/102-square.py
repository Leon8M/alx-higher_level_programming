#!/usr/bin/python3
"""
Module that contains the Square class.
"""


class Square:
    """
    Class that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square instance.

        Args:
            size (float or int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            float or int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (float or int): The size value to set.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.

        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison between two Square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Inequality comparison between two Square instances.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.

        """
        return not self == other

    def __lt__(self, other):
        """
        Less than comparison between two Square instances.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is less than the other square's area.

        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Less than or equal comparison between two Square instances.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is less than or equal to other area.

        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Greater than comparison between two Square instances.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is greater than the other area.

        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Greater than or equal comparison between two Square instances.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is greater than or equal to other area.

        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
