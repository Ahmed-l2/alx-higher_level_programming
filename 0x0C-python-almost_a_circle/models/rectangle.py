#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base.

    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int, optional): X-coordinate of the rectangle's position.
        y (int, optional): Y-coordinate of the rectangle's position.
        id (int, optional): Unique identifier for the rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle's position.
        y (int): Y-coordinate of the rectangle's position.

    Methods:
        width (getter, setter): Get or set the width of the rectangle.
        height (getter, setter): Get or set the height of the rectangle.
        x (getter, setter): Get or set x-coordinate of rectangle's position.
        y (getter, setter): Get or set y-coordinate of rectangle's position.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, attr, value, eq=True):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(attr))
        elif not eq and value < 0:
            raise ValueError("{} must be > 0".format(attr))
