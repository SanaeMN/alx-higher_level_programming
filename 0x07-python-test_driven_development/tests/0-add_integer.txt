#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b"""

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if a == float('NaN') or b == float('NaN'):
        raise ValueError('cannot convert float NaN to integer')
    s = int(a) + int(b)
    if s == a or s == b:
        raise OverflowError('cannot convert float infinity to integer')
    return s
