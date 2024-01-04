#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """An empty class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Constructor.

        Args:
            width: width atribute of the rectangle.
            height: height atribute of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value: New Width value for the rectangle.

        Raises:
            TypeError: If width or height are not an integer
            ValueError: If width or height are less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value: New height value for the rectangle.

        Raises:
            TypeError: If height or height are not an integer
            ValueError: If height or height are less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
