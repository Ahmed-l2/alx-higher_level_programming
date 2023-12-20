#!/usr/bin/python3
"""Square module."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: Size attribute of the square.
            position: Position attribute of the square.
        """

        self.size = size
        self.position = position

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square, computed as the square of the side
            length.
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return (self.__size)

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #.

        If size is equal to 0, print an empty line.
        Position should be used by adding spaces (indentation).
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")
        for y in range(0, self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for k in range(0, self.__size):
                print("#", end='')
            print("")

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            Tuple: the position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value: New position of square.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """Replicates the print() function of a Square"""
        if self.__size != 0:
            for i in range(self.__position[1]):
            print("")
        for y in range(0, self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for k in range(0, self.__size):
                print("#", end='')
            print("")
        return ("")
