#!/usr/bin/python3
"""defination of a class JSON that saves"""
import json


def save_to_json_file(my_obj, filename):
    """opens a file """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
