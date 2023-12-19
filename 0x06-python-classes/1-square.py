#!/usr/bin/python3
"""Square module."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Size atribute of the square.
        """
        try:
            self.__size = size
             if self.__size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
