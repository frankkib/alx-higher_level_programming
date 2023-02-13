#!/usr/bin/python3
"""class Square defination"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class representation"""
    def __init__(self, size, x=0, y=0, id=None):
        """class arguments"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.height

    @size.setter
    def size(self, value):
        """sets the value of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns the string representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)
