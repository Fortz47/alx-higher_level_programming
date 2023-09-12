#!/usr/bin/python3
"""
returns True if the object is an instance of a
class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """check if obj is a subclass of a_class"""
    obj_type = type(obj)
    return issubclass(obj_type, a_class) and obj_type is not a_class
