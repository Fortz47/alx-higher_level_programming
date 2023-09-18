#!/usr/bin/python3
"""A square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size, x=0, y=0, Id=None):
        """class constructor"""
        super().__init__(size, size, x, y, Id)

    def __str__(self):
        """string method to print square"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """returns size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square"""
        arg_list = ['id', 'size', 'x', 'y']
        if not (args is None or len(args) == 0):
            for i, arg in enumerate(args):
                if i >= len(arg_list):
                    break
                setattr(self, arg_list[i], arg)
        else:
            for k, v in kwargs.items():
                if k in arg_list:
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns a dictionary rep of Rectangle"""
        attr_list = ['id', 'size', 'x', 'y']
        attr = {}
        for x in attr_list:
            value = getattr(self, x)
            attr[x] = value
        return attr
