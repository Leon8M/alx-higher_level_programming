#!/usr/bin/python3
"""
Module containing add_attribute function
"""


def append_write(filename="", text=""):
    """
    Append to file
    :param filename: file
    :param text: text
    :return: lenght of text
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
