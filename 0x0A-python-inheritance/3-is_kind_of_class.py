#!/usr/bin/python3
"""Module for is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class
    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of specified class, False otherwise.
    """
    return isinstance(obj, a_class)
