#!/usr/bin/python3
"""Module for inherits_from method"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True or False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
