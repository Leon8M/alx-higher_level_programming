#!/usr/bin/python3
"""
Module containing Student class
"""


class Student:
    """
    Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize
        :param first_name: first
        :param last_name: last
        :param age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json
        :param attrs: attrs
        :return: json_dict
        """
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def reload_from_json(self, data):
        """
        Reload
        :param data: data
        :return: nothing
        """
        for key, value in data.items():
            setattr(self, key, value)
