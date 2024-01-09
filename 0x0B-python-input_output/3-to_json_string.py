#!/usr/bin/python3
"""Function for to_json_string"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj: given object

    Return:
        returns the JSON string
    """

    return json.dumps(my_obj)
