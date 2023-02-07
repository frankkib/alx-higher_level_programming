#!/usr/bin/python3
"""class with an opening file function"""


def write_file(filename="", text=""):
    """reads a text file"""
    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
