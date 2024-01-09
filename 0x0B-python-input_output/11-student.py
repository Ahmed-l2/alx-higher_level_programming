#!/usr/bin/python3
"""Module for Student Class"""


class Student:
    """Student Class representing first and last name and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        try:
            for attribute in attrs:
                if type(attribute) is not str:
                    return vars(self)
        except Exception:
            return vars(self)

        st_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                st_dict[key] = value
        return st_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            if key == "last_name":
                self.last_name = value
            if key == "age":
                self.age = value
