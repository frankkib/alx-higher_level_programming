#!/usr/bin/python3
import json
"""JSON Object defination"""


def load_from_json_file(filename):
    """creates objects"""
    with open(filename) as f:
        return json.load(f)
