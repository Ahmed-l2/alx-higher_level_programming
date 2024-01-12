#!/usr/bin/python3
"""Module for divding elements of a matrix"""


def matrix_divided(matrix, div):
    """Module for dividing elements of a matrix.

    takes a matrix (a list of lists of integers or floats) and a
    divisor (an integer or float).
    The function divides each element of the matrix by the divisor and returns
    a new matrix with the results rounded to 2 decimal places.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The divisor used for the division.

    Returns:
        list: A new matrix with each element divided by the divisor and rounded
        to 2 decimal places.

    Raises:
        TypeError: If the divisor is not a number or if any element
        in the matrix is not an integer or float.
        ZeroDivisionError: If the divisor is 0.
        TypeError: If the rows of the matrix do not have the same size.
    """

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    prevlistlen = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
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
