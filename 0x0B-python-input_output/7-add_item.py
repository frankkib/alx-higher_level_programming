#!/usr/bin/python3
"""script for adding arguments"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

name = "add_item.json"
try:
    json_list = load_from_json_file(name)
except FileNotFoundError:
    json_list = []
    json_list.extend(sys.argv[1:])
    save_to_json_file(json_list, name)
