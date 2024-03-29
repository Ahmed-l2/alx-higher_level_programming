#!/usr/bin/python3
"""Function definition for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string"""

    new_content = []

    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == "":
                break
            new_content.append(line)
            if search_string in line:
                new_content.append(new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(new_content)
