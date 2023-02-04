#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(self.__height):
            string += '#' * self.__width
            if i < (self.__height - 1):
                string += '\n'
        return string

    def __repr__(self):
        rect = ""
        rect += 'Rectangle(%d, %d)' % (self.__width, self.__height)
        return rect

    def __del__(self):
        print('Bye rectangle...')
        self.number_of_instances -= 1
