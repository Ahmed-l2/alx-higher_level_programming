#!/usr/bin/python3
"""Function definition for pascal_triangle"""


def pascal_triangle(n):
    """returns list of lists of integers representing Pascal’s triangle of n"""
    if n <= 0:
        return list()

    pascal_list = []
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            previous_row = pascal_list[-1]
            row = [1]

            for j in range(1, i):
                row.append(previous_row[j - 1] + previous_row[j])

            row.append(1)

        pascal_list.append(row)

    return pascal_list
