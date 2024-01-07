#!/usr/bin/python3
"""Module for divding elements of a matrix"""


def matrix_divided(matrix, div):

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    prevlistlen = len(matrix[0])
    for row in matrix:
        for elem in row:
              if not (isinstance(elem, int) or isinstance(elem, float)):
                  raise TypeError("matrix must be a matrix (list of lists) "
                  "of integers/floats")
        if len(row) != prevlistlen:
            raise TypeError("Each row of the matrix must have the same size")

    result_matrix = []

    for row in matrix:
        new_row = []
        for elem in row:
            new_elem = round(elem / div, 2)
            new_row.append(new_elem)
        result_matrix.append(new_row)

    return result_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

