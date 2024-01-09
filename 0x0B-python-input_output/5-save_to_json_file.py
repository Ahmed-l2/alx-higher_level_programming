#!/usr/bin/python3
"""Function definition for save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: JSON file to be written.
        filename: file to be written to.
    """

    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
