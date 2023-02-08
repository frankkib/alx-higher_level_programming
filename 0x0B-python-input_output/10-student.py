#!/usr/bin/python3
"""class defination"""


class Student:
    """class initialization"""
    def __init__(self, first_name, last_name, age):
        """representaion"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representaion of student"""
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new = {}
        for num in attrs:
            try:
                new[num] = self.__dict__[num]
            except Exception as Error:
                pass
            return new
