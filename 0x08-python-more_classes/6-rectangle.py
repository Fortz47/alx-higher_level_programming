#!/usr/bin/python3
"""a rectangle class"""


class Rectangle:
    """class that defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('heigth must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """prints the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = []
        for i in range(self.__height):
            result.append('#' * self.__width)
        return '\n'.join(result)

    def __repr__(self):
        """prints the official string rep of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """deletes an instance"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
        del self

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError('heigth must be an integer')
        if value < 0:
            raise ValueError('heigth must be >= 0')
        self.__height = value

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
