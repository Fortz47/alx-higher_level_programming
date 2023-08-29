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
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
