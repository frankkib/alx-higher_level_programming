#!/usr/bin/python3
"""define class append after"""


def append_after(filename="", search_string="", new_string=""):
    """arguments representaion"""
    string = ""
    with open(filename, encoding="utf-8") as f:
        for word in f:
            string += word
            if search_string in word:
                string += new_string
    with open(filename, 'w', encoding='utf-8') as r:
        r.write(string)
