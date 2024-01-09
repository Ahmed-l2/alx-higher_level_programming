#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """Reads the content of filename with encoding UTF-8 prints it to STDOUT

    Args:
        filename: Name of the file to be read
    """

    with open(filename, encoding='utf-8') as file:
        file_content = file.read()

    print(file_content, end="")
