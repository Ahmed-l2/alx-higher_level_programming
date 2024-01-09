#!/usr/bin/python3
"""Function definition for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string"""

    new_content = []

    with open(filename, 'r') as file:
        for line in file:
            if search_string in line:
                new_content.append(line.strip() + '\n' + new_string)
            else:
                new_content.append(line)

    with open(filename, 'w') as file:
        file.writelines(new_content)
