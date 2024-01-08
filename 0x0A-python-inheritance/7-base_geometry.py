#!/usr/bin/python3
"""Module for BaseGeometry Class"""


class BaseGeometry:
    """Empty class representing the BaseGeometry."""

    def area(self):
        """Determines the area for BaseGeometry instance

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value arguments

        Args:
            name: string
            value: given value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
