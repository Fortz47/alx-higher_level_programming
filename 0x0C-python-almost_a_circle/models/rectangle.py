#!/usr/bin/python3
"""class inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class inherits from base"""
    def __init__(self, width, height, x=0, y=0, Id=None):
        """class constructor"""
        args = {'width': width, 'height': height, 'x': x, 'y': y}
        for k, v in args.items():
            if not isinstance(v, int):
                raise TypeError(f"{k} must be an integer")
            if v <= 0 and (k == 'width' or k == 'height'):
                raise ValueError(f'{k} must be > 0')
            if v < 0 and (k == 'x' or k == 'y'):
                raise ValueError(f'{k} must be >= 0')
        super().__init__(Id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """string magig method"""
        Id = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        result = '[Rectangle] ({}) {}/{} - {}/{}'
        return result.format(Id, x, y, w, h)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns Rectangle Area"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle with #"""
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        arg_list = ['id', 'width', 'height', 'x', 'y']
        if args is None or len(args) == 0:
            j = 0
            for k, v in kwargs.items():
                if k in arg_list:
                    setattr(self, k, v)
        else:
            for i, arg in enumerate(args):
                if i >= len(arg_list):
                    break
                setattr(self, arg_list[i], arg)

    def to_dictionary(self):
        """returns a dictionary rep of Rectangle"""
        attr_list = ['id', 'width', 'height', 'x', 'y']
        attr = {}
        for x in attr_list:
            value = getattr(self, x)
            attr[x] = value
        return attr
