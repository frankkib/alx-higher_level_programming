#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict ={}
    for key,number in a_dictionary.items():
        new_dict[key] = number * 2
        return new_dict
