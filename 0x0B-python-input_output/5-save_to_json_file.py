#!/usr/bin/python3
"""Defines a JSON file-writing function"""


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(file=filename, mode='w') as file:
        from json import dump
        dump(my_obj, file)
