#!/usr/bin/python3
"""Defines a square-printing function"""


def print_square(n):
    """Print a square with the # character
    :param n:
    :type : integer
    :return: none
    :rtype: none
    """
    if type(n) is not int:
        raise TypeError('size must be an integer')
    if n < 0:
        raise ValueError('size must be >= 0')
    if n == 0:
        print()
    for _ in range(n):
        print('#' * n)
