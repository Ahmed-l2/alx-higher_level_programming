#!/usr/bin/python3
"""Module for text_indentation"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".?:":
        text = (delimiter + "\n\n").join(
                [line.strip(" ") for line in text.split(delimiter)])
    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
