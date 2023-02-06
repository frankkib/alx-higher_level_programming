#!/usr/bin/python3
"""Mylist class defination"""


class MyList(list):
    """intialization and defination of the subclass"""
    def __init__(self):
        """object initialization"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
