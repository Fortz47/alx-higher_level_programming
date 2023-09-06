#!/usr/bin/python3
"""creates a locked class"""


class LockedClass:
    """creates a locked class"""
    def __setattr__(self, name, value):
        """sets an attribute"""
        error = "'LockedClass' object has no attribute"
        if name != 'first_name':
            raise AttributeError(f"{error} '{name}'")
        self.__dict__[name] = value
