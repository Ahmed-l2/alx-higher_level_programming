#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """writes to filename with encoding UTF-8

    Args:
        filename: Name of the file to be read
        text: text to be written to file
    """

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
