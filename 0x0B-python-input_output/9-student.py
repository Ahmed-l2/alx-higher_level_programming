#!/usr/bin/python3
"""Module for Student Class"""


class Student:
    """Student Class representing first and last name and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return vars(self)
