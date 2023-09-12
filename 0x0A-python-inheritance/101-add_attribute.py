#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    """adds a new attribute to an object if it’s possible"""
    if type(obj) is type:
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
