#!/usr/bin/python3
"""Function definition for load_from_json_file"""


def load_from_json_file(filename):
    """Creates an Object from a “JSON file

    Args:
        filename: name of JSON file

    Returns:
        Object created from JSON file
    """

    with open(filename, 'r') as file:
        return json.loads(file.read())
