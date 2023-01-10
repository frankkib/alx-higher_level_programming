#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_list = my_list[0]
    for number in my_List:
        if number > max_list:
            max_list = number
            return (max_list)
