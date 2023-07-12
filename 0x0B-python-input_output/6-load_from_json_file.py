#!/usr/bin/python3
"""Defines a JSON file-reading function"""


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(file=filename, mode='r') as file:
        from json import load
        obj = load(file)
    return obj
