#!/usr/bin/python3
"""Square module documentation"""


class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the class"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.size = size
        if (not isinstance(position, tuple) or len(position) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif any(not isinstance(x, int) or (x < 0) for x in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.position = position

    def __str__(self):
        result = ""
        if self.__size == 0:
            pass
            # result += '\n'
        else:
            for _ in range(self.__position[1]):
                result += '\n'
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size
                result += '\n' if _ < self.__size - 1 else ''
        return result

    def __repr__(self):
        result = ""
        if self.__size == 0:
            pass
            # result += '\n'
        else:
            for _ in range(self.__position[1]):
                result += '\n'
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size
                result += '\n' if _ < self.__size - 1 else ''
        return result

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
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position"""
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        if any(not isinstance(x, int) or (x < 0) for x in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
