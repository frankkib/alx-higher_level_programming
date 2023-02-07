#!/usr/bin/python3
"""class defination that appends to a characters to a text"""


def append_write(filename="", text=""):
    """apending string"""
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
