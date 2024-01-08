#!/usr/bin/python3
"""Module for MyList method"""


class MyList(list):
    """Custom class that inherits from the list class."""

    def print_sorted(self):
        """Print the sorted elements of the list."""
        print(sorted(self))
