#!/usr/bin/python3
"""Defines a string-to-JSON function"""


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    from json import dumps
    return dumps(my_obj)
