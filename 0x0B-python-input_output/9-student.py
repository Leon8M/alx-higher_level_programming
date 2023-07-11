#!/usr/bin/python3
"""
Module containing Student class
"""


json = __import__("json")


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

    def to_json(self):
        """
        to json
        :return: json_dict
        """
        json_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return json_dict
