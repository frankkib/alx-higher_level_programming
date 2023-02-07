#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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
