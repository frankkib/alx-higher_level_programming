#!/usr/bin/python3
"""class defination module"""


class Rectangle:
    """class instatiation"""
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
        """collects the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """collects the height of the rectangle"""
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
        """finds the area of the perimeter"""
        return self.__width * self.__height

        def perimeter(self):
            """finds the perimeter of the rectangle"""
            if self.__width == 0 or self.__height == 0:
                return (0)
            else:
                return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints a string rectangle"""
        rct = ""
        wid = self.__width
        heig = self.__height
        if wid == 0 or heig == 0:
            return rct
        else:
            for height in range(heig):
                for width in range(wid):
                    rct += "#"
                    if ((width + 1) == (wid)) and ((height + 1) != (heig)):
                        rct += "\n"
            return rct

    def __repr__(self):
        """recreating the rectangle instance"""
        width = self.__width
        height = self.__height
        return "Rectangle(" + str(width) + ", " + str(height) + ")"
