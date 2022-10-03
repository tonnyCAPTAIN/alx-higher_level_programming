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

        lt = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
        """str to list"""
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                lt.append(cls.create(**item))
            else:
                lt.append(item)
        return lt

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a list of instances to a csv file.
        Args:
        list_objs (list): A list of inherited instances.
        """

        
        from .rectangle import Rectangle
        from .square import Square
        listcpy = list_objs.copy()
        for idx in range(len(listcpy)):
            listcpy[idx] = listcpy[idx].to_dictionary()
        if cls is Rectangle:
            with open("Rectangle.csv", "w") as f:
                csvwriter = csv.writer(f)
                for dicty in listcpy:
                    newlist = []
                    newlist.append(dicty["id"])
                    newlist.append(dicty["width"])
                    newlist.append(dicty["height"])
                    newlist.append(dicty["x"])
                    newlist.append(dicty["y"])
                    csvwriter.writerow(newlist)
        if cls is Square:
            with open("Square.csv", "w") as f:
                csvwriter = csv.writer(f)
                for dicty in listcpy:
                    newlist = []
                    newlist.append(dicty["id"])
                    newlist.append(dicty["size"])
                    newlist.append(dicty["x"])
                    newlist.append(dicty["y"])
                    csvwriter.writerow(newlist)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list of instances from a csv file.
        Returns:
        List of classes inheriting from base class.
        """

        from .rectangle import Rectangle
        from .square import Square
        if cls is Rectangle:
            with open("Rectangle.csv", "r") as f:
                csvreader = csv.reader(f)
                retlist = []
                for row in csvreader:
                    newrect = Rectangle(int(row[1]), int(row[2]), int(row[3]),
                                        int(row[4]), row[0])
                    retlist.append(newrect)
                return retlist
        elif cls is Square:
            with open("Square.csv", "r") as f:
                csvreader = csv.reader(f)
                retlist = []
                for row in csvreader:
                    newsquare = Square(int(row[1]), int(row[2]),
                                       int(row[3]), row[0])
                    retlist.append(newsquare)
                return retlist

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
