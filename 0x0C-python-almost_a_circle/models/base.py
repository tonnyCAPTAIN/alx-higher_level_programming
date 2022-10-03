#!/usr/bin/python3
"""Creating class called Base"""

import json
import csv
import turtle


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

        json_file = cls.__name__ + ".json"
        with open(json_file, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                obj_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(obj_dicts))

    @staticmethod
    def from_json_string(json_string):
        """return JSON string"""

        if json_string is None or json_string == "[]":
            return []
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

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """

        filename = cls.__name__ + ".csv"
        with open(filename, encoding="utf-8", mode="w") as fp:
            writer = csv.writer(fp)
            rows = []
            if list_objs is not None and type(list_objs) is list:
                for obj in list_objs:
                    row = []
                    row.append(obj.id)
                    if cls.__name__ == "Rectangle":
                        row.append(obj.width)
                        row.append(obj.height)
                    if cls.__name__ == "Square":
                        row.append(obj.size)
                    row.append(obj.x)
                    row.append(obj.y)
                    rows.append(row)
            writer.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """

        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', newline='') as csvfile:
                if cls.__name__ == "Rectangle":
                    keynames = ["id", "width", "height", "x", "y"]
                else:
                    keynames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=keynames)
                list_dicts = [dict([k, int(v)] for k, v in
                              d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

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
