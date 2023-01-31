#!/usr/bin/python3
"""Rectangle class defination"""


class Rectangle:
    """class initialization"""

    def __init__(self, width=0, height=0):
        """new rectangle
        Args:
            width (int)
            height (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """collects the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """collects the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
