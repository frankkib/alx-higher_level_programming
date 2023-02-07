#!/usr/bin/python3
"""class defination of function that opens a file"""


def read_file(filename=""):
    """"prints the contents of UTF8 text"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
