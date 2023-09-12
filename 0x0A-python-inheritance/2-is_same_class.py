#!/usr/bin/python3
"""
returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """check if obj is an instance of a_class"""
    return isinstance(obj, a_class) and a_class is not object
