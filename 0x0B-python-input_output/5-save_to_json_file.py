#!/usr/bin/python3
"""
Module containing add_attribute function
"""


json = __import__("json")


def save_to_json_file(my_obj, filename):
    """
    Save json
    :param my_obj: obj
    :param filename: file
    :return: nothing
    """
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
