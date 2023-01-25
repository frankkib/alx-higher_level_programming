#!/usr/bin/python3
"""class defination"""
class Square:
    """"defines square attributes"""
    def __init__(self, size):
        """initializes the square"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("ize must be >= 0")
        self.__size = size
