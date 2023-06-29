#!/usr/bin/python3
"""Defines a Square file"""


class Square:
    """Represent a square class"""

    def __init__(self, n=0, position=(0, 0)):
        """class constructor"""
        self.__size = n
        self.__position = position

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

    @property
    def position(self):
        """position getter"""
        return (self.__position)

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) or len(position) != 2 or
            type(position[0]) is not int or type(position[-1]) is not int or
            position[0] < 0 or position[-1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.position[-1]):
            print("")
        for _ in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
