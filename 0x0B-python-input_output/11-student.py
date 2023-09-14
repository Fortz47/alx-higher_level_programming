#!/usr/bin/python3
"""class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
        a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if isinstance(json, dict):
            for k, v in json.items():
                if k in ['first_name', 'last_name', 'age']:
                    self.k = v

