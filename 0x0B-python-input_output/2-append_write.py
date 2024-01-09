#!/usr/bin/python3
"""append_file function"""


def append_write(filename="", text=""):
    """appends text to filename with encoding UTF-8

    Args:
        filename: Name of the file to be read
        text: text to be appened to file
    """

    with open(filename, 'a', encoding='utf-8') as file:
        return file.append(text)
