#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, identifier=None):
        """Initialize a new Rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(identifier)

    @property
    def width(self):
        """Set/get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle using the `#` character"""
        str_format = self.__y * "\n"
        for _ in range(self.__height):
            str_format += (" " * self.__x)
            str_format += ("#" * self.__width) + "\n"
        print(str_format, end='')

    def __str__(self):
        """Return the print() and str() representation of the Rectangle"""
        str_rectangle = f"[{self.__class__.__name__}] "
        identifier = f"({self.id}) "
        x_y = f"{self.__x}/{self.__y} - "
        w_h = f"{self.__width}/{self.__height}"

        return str_rectangle + identifier + x_y + w_h

    def update(self, *args, **kwargs):
        """Update the Rectangle"""
        if args is not None and len(args) > 0:
            keys = ['id', 'width', 'height', 'x', 'y']
            for key, value in zip(keys, args):
                setattr(self, key, value)
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {k: getattr(self, k)
                for k in ['x', 'width', 'id', 'height', 'y']}
