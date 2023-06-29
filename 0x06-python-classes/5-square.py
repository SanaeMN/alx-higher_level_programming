#!/usr/bin/python3
"""Defines a Square file"""


class Square:
    """Represent a square class"""

    def __init__(self, n=0):
        """class constructor"""
        self.__size = n

    def area(self):
        """Return current area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """getter/setter current size"""
        return (self.__size)

    @size.setter
    def size(self, n):
        if not isinstance(n, int):
            raise TypeError('size must be an integer')
        if n < 0:
            raise ValueError('size must be >= 0')
        self.__size = n

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print("")
        for _ in range(self.__size):
            print('#' * self.__size)
