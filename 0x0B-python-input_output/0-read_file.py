#!/usr/bin/python3


def read_file(filename=""):
    """Reads the content of a text file prints it to STDOUT

    Args:
        filename: Name of the file to be read
    """

    with open(filename, 'r') as file:
        file_content = file.read()

    print(file_content)
