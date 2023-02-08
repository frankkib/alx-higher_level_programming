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
