#!/usr/bin/python3
"""
Module containing Student class
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append
    :param filename: name
    :param search_string: string
    :param new_string: new string
    :return: nothing
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
