#!/usr/bin/python3
"""Module for class_to_json"""


def class_to_json(obj):
    """Creates dictionary description with simple data structure (list, dict,
    string, integer and boolean) for JSON serialization of an object

    Args:
        obj: given object

    Returns:
        JSON serialization of an object
    """

    return vars(obj)
