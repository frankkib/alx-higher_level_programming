#!/usr/bin/python3
"""JSON Object defination"""


def load_from_json_file(filename):
    """creates objects"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
