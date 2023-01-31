#!/usr/bin/python3
"""class  defination module"""


class Rectangle:
    """class instantiation """
    def __init__(self, width=0, height=0):
        """class initialization
        Args:
            (int) __width
            (int) __height
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """collects the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """collects the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """finds the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """finds the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))
