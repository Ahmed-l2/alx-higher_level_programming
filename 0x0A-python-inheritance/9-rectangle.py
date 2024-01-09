#!/usr/bin/python3
"""Module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Contructor

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation method"""
        return ("[Rectangle] {}/{}".format(str(self.__width),
                str(self.__height)))
