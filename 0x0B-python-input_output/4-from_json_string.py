#!/usr/bin/python3
"""Function definition for from_json_string"""
import json


def from_json_string(my_str):
    """Creates a Python representation of a JSON string

    Args:
        my_str: JSON string

    Return:
        returns Python representation of JSON string
    """

    return json.loads(my_str)
