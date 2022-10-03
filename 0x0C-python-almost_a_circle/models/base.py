#!/usr/bin/python3
"""Creating class called Base"""

import json
import csv


class Base:
    '''Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''class method'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON sting representation"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write into a file JSON string"""

        with open(cls.__name__ + ".json", mode="w") as write_file:
            if list_objs is None:
                write_file.write("[]")
            else:
               # Using to_json_string(), and to_dictionary() to format
               write_file.write(cls.to_json_string(
                   [item.to_dictionary() for item in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """return JSON string"""

        if type(json_string) != str or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return list instances"""

        lt = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
        #str to list
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                lt.append(cls.create(**item))
            else:
                lt.append(item)
        return lt

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file"""

        lt = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, lt[0].keys())
            write_to.writeheader()
            write_to.writerows(lt)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a Turtle window and draws
        and draws rectangles and square
        Args:
            list_rectangle
            list_square
        """

        turtle.speed(3)
        t = turtle.Turtle()
        t.color("blue")
        t.hideturtle()
        for rect_objs in list_rectangles:
            t.up()
            t.setx(rect_objs.x)
            t.sety(rect_objs.y)
            t.down()
            for i in range(2):
                t.fd(rect_objs.width)
                t.lt(90)
                t.fd(rect_objs.height)
                t.lt(90)

        for sq_objs in list_squares:
            t.up()
            t.setx(sq_objs.x)
            t.sety(sq_objs.y)
            t.down()
            for i in range(2):
                t.fd(sq_objs.width)
                t.lt(90)
                t.fd(sq_objs.height)
                t.lt(90)

        turtle.exitonclick()
