#!/usr/bin/python3
"""Square module documentation"""


class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0):
        """initializes the class"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """returns the current area"""
        return self.__size ** 2
