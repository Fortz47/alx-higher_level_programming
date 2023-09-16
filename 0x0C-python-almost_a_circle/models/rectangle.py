#!/usr/bin/python3
"""class inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class inherits from base"""
    def __init__(self, width, height, x=0, y=0, Id=None):
        """class constructor"""
        super().__init__(Id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__heigth

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.__y = value
