#!/usr/bin/python3
""" Module that contains class Base """
from json import dumps, loads
from os import path
import csv
import turtle


class Base:
    """Defines a base model class"""
    __nb_objects = 0

    def __init__(self, identifier=None):
        """Initialize a new Base"""
        if identifier is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = identifier

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes"""
        obj = cls(1, 1) if cls.__name__ == 'Rectangle' else cls(1)
        obj.update(**dictionary)
        return obj

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts"""
        if list_dictionaries is None or type(list_dictionaries) != list\
                or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file"""
        list_dic = []
        if list_objs is not None:
            list_dic = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", mode='w') as file:
            file.write(f'{cls.to_json_string(list_dic)}')

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string"""
        if not json_string:
            return []
        return loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings"""
        filename = f"{cls.__name__}.json"
        if not path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_str = f.read()
        return [cls.create(**dct) for dct in cls.from_json_string(list_str)]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file"""
        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        else:
            keys = ('id', 'size', 'x', 'y')
        with open(f"{cls.__name__}.csv", 'w') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file"""
        filename = f"{cls.__name__}.csv"
        objects = []
        if not path.exists(filename):
            return objects
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            c = True
            for row in reader:
                if c:
                    c = False
                    keys = row[:]
                else:
                    dic = {keys[i]: int(value) for i, value in enumerate(row)}
                    objects.append(cls.create(**dic))
        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module"""
        t = turtle.Turtle()
        t.screen.bgcolor('#000000')
        t.shape('turtle')
        t.color('#ffffff')
        t.penup()
        t.goto(-200, 200)
        for rect in list_rectangles:
            t.goto(t.xcor() + (rect.width + 20), t.ycor() - (rect.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()
        t.goto(-200, -20)
        for squ in list_squares:
            t.goto(t.xcor() + (squ.width + 20), t.ycor() - (squ.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(squ.width)
                t.left(90)
                t.forward(squ.height)
                t.left(90)
            t.penup()
        t.Screen().exitonclick()
