#!/usr/bin/python3
"""Module for Square Method"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass that inherits from the Rectangle Class"""
    def __init__(self, size):
        """Constructor

        Args:
            size: size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method to retrieve area of Square"""
        return self.__size ** 2
