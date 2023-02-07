#!/usr/bin/python3
"""BaseGeometry class defination"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle initialization"""
    def __init__(self, width, height):
        """instantation """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Finds area """
        return self.__width * self.__height

    def __str__(self):
        """string representaion"""
        return "[Rectangl] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square initialization"""
    def __init__(self, size):
        """Instantation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """finds the area of the Square"""
        return self.__size * self.__size

    def __str__(self):
        """string representation"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
