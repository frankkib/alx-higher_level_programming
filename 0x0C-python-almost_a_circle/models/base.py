#!/usr/bin/python3
"""class Base defination"""
import json


class Base:
    __nb_objects = 0

    """class intialization"""
    def __init__(self, id=None):
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """JSON string representation """
        if (list_dictionaries is None) or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
