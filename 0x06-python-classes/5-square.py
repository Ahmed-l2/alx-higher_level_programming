#!/usr/bin/python3
"""Square module."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Size attribute of the square.
        """

        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square, computed as the square of the side
            length.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: New size value for the square.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()
