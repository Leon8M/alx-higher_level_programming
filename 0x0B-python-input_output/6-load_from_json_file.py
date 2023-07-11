#!/usr/bin/python3
"""
Module containing add_attribute function
"""


json = __import__("json")


def load_from_json_file(filename):
    """
    Load json
    :param filename: file name
    :return: json load file
    """
    with open(filename, mode='r') as file:
        return json.load(file)
