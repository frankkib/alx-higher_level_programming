#!/usr/bin/python3
""" class defination module"""


class LockedClass:
    """ prevents the user from dynamically creating new instance attributes"""
    __slots__ = ['first_name']
