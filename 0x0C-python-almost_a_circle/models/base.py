#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, Id=None):
        """class constructor"""
        if Id is not None:
            self.id = Id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
