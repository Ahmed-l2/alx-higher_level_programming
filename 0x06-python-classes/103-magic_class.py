#!/usr/bin/python3
"""Recreating MagiClass from 10. ByteCode -> Python #5"""
import math


class MagicClass:
    """Class that represents a circle"""

    def __init__(self, radius=0):
        """Takes the radius

        Arg:
            radius: takes the radius of the circle (float or int)
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """returns the area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """returns the circumference of the circle."""
        return (2 * math.pi * self.__radius)
