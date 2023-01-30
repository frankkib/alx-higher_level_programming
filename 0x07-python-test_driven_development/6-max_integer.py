#!/usr/bin/python3
"""module for finding maximum number"""


def max_integer(list=[]):
    if len(list) == 0:
        return None
    max_number = list[0]
    index = 1
    while index < len(list):
        if list[index] > max_number:
            max_number = list[index]
            index += 1
    return max_number
