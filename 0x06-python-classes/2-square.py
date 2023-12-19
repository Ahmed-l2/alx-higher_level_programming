#!/usr/bin/python3
"""Square module."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Size atribute of the square.

        Raises:
            TypeError: If size is not an int
            ValueError: If size is less than 0
        """
        try:
            self.__size = size
            if not isinstance(self.__size, int):
                raise TypeError("size must be an integer")
            if self.__size < 0:
                raise ValueError("size must be >= 0")
