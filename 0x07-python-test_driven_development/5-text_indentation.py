#!/usr/bin/python3
"""Module for text_indentation"""


def text_indentation(text):
    """Module for adding indentation to text based on delimiters.

    This module provides a function, text_indentation, which takes a string
    (text) as a parameter and adds indentation based on specified delimiters
    (".", "?", ":").

    Args:
        text (str): The input text to be formatted. Must be a string.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".?:":
        text = (delimiter + "\n\n").join(
                [line.strip(" ") for line in text.split(delimiter)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
