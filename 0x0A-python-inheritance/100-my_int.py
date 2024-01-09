#!/usr/bin/python3
"""Module for MyInt Method"""


class MyInt(int):
    """
    A custom subclass of int with swapped behavior for equality operators.

    Args:
        value (int): The integer value for initialization.
    """
    def __new__(cls, value):
        """
        Creates a new instance of MyInt.

        Args:
            cls: The class.
            value (int): The integer value for initialization.

        Returns:
            MyInt: A new instance of MyInt.
        """
        return super().__new__(cls, value)

    def __eq__(self, other):
        """
        Customizes the behavior of the equality operator (==).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the values are not equal; otherwise, False.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Customizes the behavior of the not equal operator (!=).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the values are equal; otherwise, False.
        """
        return not super().__ne__(other)
