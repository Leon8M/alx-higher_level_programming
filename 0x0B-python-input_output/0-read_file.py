#!/usr/bin/python3
"""
Module containing add_attribute function
"""


def read_file(filename=""):
    """
    Read file.
    :param filename: name of file
    :return: nothing
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
