#!/usr/bin/python3
"""BaseGeometry, Rectangle and square class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializes the class"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def __str__(self):
        """prints rectangle"""
        return f'[Rectangle] {self.__width}/{self.__height}'

    def area(self):
        """returns the area"""
        return self.__width * self.__height


class Square(Rectangle):
    """inherits from Rectangle class"""
    def __init__(self, size):
        """initializes the class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints square"""
        return f'[Square] {self.__size}/{self.__size}'

    def area(self):
        """returns the square area"""
        return self.__size ** 2
