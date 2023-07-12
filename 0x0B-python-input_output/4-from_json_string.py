#!/usr/bin/python3
"""Defines a JSON-to-object function"""


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    from json import loads
    return loads(my_str)
