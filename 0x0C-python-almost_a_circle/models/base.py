#!/usr/bin/python3
"""creating classes for unit testing"""


class Base:
    """creating a class, base"""

    __nb_objects = 0;

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
