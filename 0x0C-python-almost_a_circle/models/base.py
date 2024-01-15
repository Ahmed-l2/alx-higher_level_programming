#!/usr/bin/python3
"""Module for the Base class"""
import json
import csv


class Base:
    """Base class for object counting.

    Args:
        id: Object ID. If provided, assigned to 'id' attribute.
        If not provided, '__nb_objects' is incremented and assigned.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """contructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts dictionary to json string"""
        if list_dictionaries is None:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes Json string representation of list_objs to Json file."""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy_instance = Rectangle(1, 1)
        elif cls is Square:
            dummy_instance = Square(1)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances;"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, 'r', encoding="utf-8") as f:
            return [cls.create(**dic) for dic in
                    cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save Object to CSV file"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [
                            [obj.id, obj.width, obj.height, obj.x, obj.y]
                            for obj in list_objs]
            else:
                list_objs = [
                        [obj.id, obj.size, obj.x, obj.y] for obj in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Load object from CSV file"""
        from models.rectangle import Rectangle
        from models.square import Square
        csv_string = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='uttf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    dct = {
                            "id": row[0],
                            "width": row[1],
                            "height": row[2],
                            "x": row[3],
                            "y": row[4]
                            }
                else:
                    dct = {
                            "id": row[0],
                            "size": row[1],
                            "x": row[2],
                            "y": row[3]
                            }
                csv_string.append(cls.create(**dct))
        return csv_string
