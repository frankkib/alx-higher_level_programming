#!/usr/bin/python3
"""inherits class defination"""


def inherits_from(obj, a_class):
    """returns the sub class of  the object"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
