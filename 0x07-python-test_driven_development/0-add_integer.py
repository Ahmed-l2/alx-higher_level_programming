#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """
    Addition function.

    Adds two integer, 'x' and 'y' and returns the value of the addition

    Args:
        a: first integer.
        b: second integer, defaults to 98.

    Raises:
        TypeError: if a or/and b are not an integer or float.

    Returns:
        the sum of the addition.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
