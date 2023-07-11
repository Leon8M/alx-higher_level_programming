#!/usr/bin/python3
"""
Module containing add_attribute function
"""


def class_to_json(obj):
    """
    Class to json
    :param obj: obj
    :return: json-dict
    """
    json_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
