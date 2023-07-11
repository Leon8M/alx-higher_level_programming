#!/usr/bin/python3
"""
Module containing add_attribute function
"""


def write_file(filename="", text=""):
    """
    write file
    :param filename: file
    :param text: text
    :return: length of text
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
