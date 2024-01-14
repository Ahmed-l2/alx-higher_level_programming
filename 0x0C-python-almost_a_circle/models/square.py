#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor

        Args:
            size: Size of square
            x: x position of Square
            y: y positions of Square
            id: inherited instance attribute
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the value of size"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Helper method that updates instance attributes via *args/**kwargs"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Reassigns an argument to each attribute"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def __str__(self):
        """String Representation of Square Class"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.size))
