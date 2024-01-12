#!/usr/bin/python3
"""Module for the Base class"""


class Base:
    """Base class for object counting.

    Args:
        id: Object ID. If provided, assigned to 'id' attribute.
        If not provided, '__nb_objects' is incremented and assigned.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
