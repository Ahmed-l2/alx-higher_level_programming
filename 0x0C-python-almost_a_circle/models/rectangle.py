#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x of the rectange.
            y (int, optional): y of rectangle.
            id (int, optional): id attribute inherited from Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle."""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle."""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """get x of rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """set x of rectangle's position."""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """get y of rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """set y of rectangle's position."""
        self.validate_integer("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        print(rectangle_str.rstrip("\n"))

    def validate_integer(self, attr, value, eq=True):
        """Validate that the given value is an integer and satisfies optional
            equality constraint.

        Args:
            attr (str): Name of the attribute being validated.
            value: Value to be validated.
            eq (bool, optional): Whether the value must be greater than or
            equal to zero (default) or greater than zero.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to zero
            (eq=True) or greater than zero (eq=False).
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(attr))
        elif not eq and value < 0:
            raise ValueError("{} must be > 0".format(attr))
