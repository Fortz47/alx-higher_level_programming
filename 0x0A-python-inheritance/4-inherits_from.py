#!/usr/bin/python3
"""check if obj is a subclass of a_class"""


def inherits_from(obj, a_class):
    """check if obj is a subclass of a_class"""
    if type(obj) is a_class:
        return False
    for base in type(obj).__bases__:
        if base is a_class or inherits_from(base, a_class):
            return True
    return False
