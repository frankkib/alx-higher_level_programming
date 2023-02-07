#!/usr/bin/python3
"""Importing class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle
"""class Square inherits Rectangle"""


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
