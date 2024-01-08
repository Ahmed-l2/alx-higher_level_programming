#!/usr/bin/python3
"""Module for is_same_class method"""

def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of the specified class, False otherwise.
    """
    return type(obj) == a_class
