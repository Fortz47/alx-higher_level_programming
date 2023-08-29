#!/usr/bin/python3

class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the class"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        if not isinstance(position, tuple) or len(position) < 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(position[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(position[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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
            print(' ' * self.__position[0], end='')
            for j in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position"""
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(value[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
