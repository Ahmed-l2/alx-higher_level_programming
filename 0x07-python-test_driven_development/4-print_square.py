#!/usr/bin/python3
"""Module for print_square"""


def print_square(size):
    """Module for printing a square of a given size.

    This module provides a function, print_square, which takes an integer
    (size) as a parameter and prints a square of '#' characters with the
    specified size.

    Args:
        size (int): The size of the square. Must be a non-negative integer.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is a negative integer.
        TypeError: If the size is a float.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for column in range(size):
        for row in range(size):
            print('#', end="")
        print("")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
