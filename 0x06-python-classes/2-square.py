#!/usr/bin/python3

class Square:
    """defines a square"""

    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
    
