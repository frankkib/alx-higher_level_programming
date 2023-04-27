#!/usr/bin/python3
"""module for peaking a list"""


def find_peak(list_of_integers):
    """class defination and parameters"""
    num = len(list_of_integers)
    if num == 0:
        return None
    if num == 1:
        return list_of_integers[0]
    if num == 2:
        return max(list_of_integers)

    middle = num // 2
    if list_of_integers[middle] < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
    elif list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle + 1:])
    else:
        return list_of_integers[middle]
