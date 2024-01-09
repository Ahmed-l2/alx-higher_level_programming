#!/usr/bin/python3
"""Module for add_attribute method"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if it’s possible.

    Args:
        object: given object
        attr: attribute to be added to object
        value: value of attribute

    Raises:
        TypeError: if attribute cannot be added to object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
