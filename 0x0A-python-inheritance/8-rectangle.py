#!/usr/bin/python3
"""Importing class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""class  Rectangle that inherits BaseGeometry"""


class Rectangle(BaseGeometry):
    """Rectangle initialization"""
    def __init__(self, width, height):
        """instantation """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
