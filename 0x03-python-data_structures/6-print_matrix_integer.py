#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for lst in matrix:
        for num in lst:
            end_char = " " if num != lst[-1] else ""
            print("{:d}".format(num), end=end_char)
        print("")
