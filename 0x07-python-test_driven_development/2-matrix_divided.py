#!/usr/bin/python3
"""
Module with matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides elements in a matrix and divides by given divisor.
    :param matrix: the matrix to be added.
    :param div: the divisor.
    :return: rounded value to two decimal places of the quotient.
    :raises:TypeError: if matrix is a list of lists of integers or floats.
            TypeError: if each row of the matrix is not of the same size.
            ZeroDivisionError: if div is equal to zero.
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
