#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak of a list"""
    if not list_of_integers:
        return None
    result = 0
    for num in list_of_integers:
        if (num >= result):
            result = num
    return result
