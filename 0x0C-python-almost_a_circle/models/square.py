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
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = self.width

    def __str__(self):
        """String Representation of Square Class"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.size))
