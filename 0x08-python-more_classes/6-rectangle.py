#!/usr/bin/python3
"""Defines a Rectangle module"""


class Rectangle:
    """Represent a Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.__height * self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ""

        representation = ''
        for i in range(self.__height):
            representation += '#' * self.__width
            if i != self.__height - 1:
                representation += '\n'
        return representation

    def __repr__(self):

        s = 'Rectangle(' + str(self.__width)
        s += ', ' + str(self.__height) + ')'
        return s

    def __del__(self):

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
