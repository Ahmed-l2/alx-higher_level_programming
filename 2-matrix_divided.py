#!/usr/bin/python3
"""Module for divding elements of a matrix"""


def matrix_divided(matrix, div):

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0
        raise ZeroDivisionError("division by zero")
    for lists in matrix:
        for inf in lists:
              if not (isinstance(inf, int) or isinstance(inf, float)):
                  raise TypeError("matrix must be a matrix (list of lists)
                  of integers/floats")
        prevlistlen = len(lists)
