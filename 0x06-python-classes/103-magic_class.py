#!/usr/bin/python3
"""A module doc"""
import math


class MagicClass:
    """a class that defines a circle"""
    def __init__(self):
        """initializes the class"""
        self.__radius = 0

    @property
    def radius(self):
        """retrieves the radius"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """sets the radius"""
        if not isinstance(value, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        """returns the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """returns the circumference"""
        return 2 * math.pi * self.__radius
