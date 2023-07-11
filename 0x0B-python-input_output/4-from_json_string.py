#!/usr/bin/python3
"""
Module containing add_attribute function
"""


json = __import__('json')


def from_json_string(my_str):
    return json.loads(my_str)
