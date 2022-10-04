#!/usr/bin/python3
""" Define a base class """
import json
import csv
import turtle


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """

        filename = cls.__name__ + ".json"
        export_list = []
        with open(filename, "w") as new_file:
            if list_objs is None:
                return new_file.write("[]")
            else:
                for i in list_objs:
                    # export_list.append(Base.to_dictionary(i))
                    export_list = [i.to_dictionary() for i in list_objs]
                new_file.write(Base.to_json_string(export_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """

        if (dictionary):
            if cls.__name__ == 'Rectangle':
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """

        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    keynames = ["id", "width", "height", "x", "y"]
                else:
                    keynames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=keynames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

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
