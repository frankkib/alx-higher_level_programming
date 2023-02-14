#!/usr/bin/python3
"""class Base defination"""
import json


class Base():
    """class Base defination"""
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
    def to_json_string(list_dictionaries):
        """JSON string representation """
        if (list_dictionaries is None) or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        obj_dict = []

        if list_objs is not None:
            for obj in list_objs:
                obj_dict.append(cls.to_dictionary(obj))
                with open(filename, 'w') as f:
                    f.write(cls.to_json_string(obj_dict))

    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
