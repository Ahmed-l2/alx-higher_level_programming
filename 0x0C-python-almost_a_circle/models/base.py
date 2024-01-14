#!/usr/bin/python3
"""Module for the Base class"""
import json


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
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, 'r', encoding="utf-8") as f:
            return [cls.create(**dic) for dic in cls.from_json_string(f.read())]
