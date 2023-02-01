#!/usr/bin/pyhton3
"""module for printing a square"""


def print_square(size):
    """args
        @size: size of the square
        """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for length in range(size):
        for width in range(size):
            print("#", end="")
        print()
