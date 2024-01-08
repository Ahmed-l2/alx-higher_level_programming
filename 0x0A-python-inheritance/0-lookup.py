#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """
    Retrieve a list of attributes and methods of an object.

    Args:
        obj (object): The input object for which attributes and methods
        are retrieved.

    Returns:
        list: A list containing the names of attributes and methods
        associated with the object.
    """
    return dir(obj)
