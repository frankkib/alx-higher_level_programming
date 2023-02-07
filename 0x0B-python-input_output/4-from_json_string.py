#!/usr/bin/python3
"""class defination for JSON """
import json


def from_json_string(my_str):
    """returns an object represented by JSON"""
    return json.loads(my_str)
