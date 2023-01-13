#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for index in list(a_dictionary):
        if a_dictionary.get(index) == value:
            del a_dictionary[index]
