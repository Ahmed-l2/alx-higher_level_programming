#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """An class representing a rectangle."""

    number_of_instances = 0
    """int: A class attribute to track the number of instances created.

    This attribute is incremented when a new instance
    is created and decremented when an instance is deleted.
    """

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor.

        Args:
            width: width atribute of the rectangle.
            height: height atribute of the rectangle.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Calculates the area of the rectangle

        Returns:
            int: The Area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle

        Returns:
            int: The Perimeter of the rectangle
        """

        if (self.__width == 0 or self.__height == 0):
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of the rectangle."""
        if (self.__width == 0 or self.__height == 0):
            return ""

        if hasattr(self, 'print_symbol'):
            symbol = self.print_symbol
        else:
            symbol = Rectangle.print_symbol
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(symbol) * self.__width + "\n"
        return rectangle_str.rstrip("\n")

    def __repr__(self):
        """Developer-friendly representation of the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes the instances"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the greater or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the greater or equal area.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance representing a square.

        Args:
            size (int): Size of the square.

        Returns:
            Rectangle: A new Rectangle instance with equal width and height.
        """
        return cls(size, size)
