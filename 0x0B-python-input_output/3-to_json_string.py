#!/usr/bin/python3
"""
Module containing add_attribute function
"""


json = __import__('json')


def to_json_string(my_obj):
    """
    to json
    :param my_obj: obj
    :return: obj json
    """
    return json.dumps(my_obj)
