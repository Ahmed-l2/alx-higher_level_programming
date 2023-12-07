#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    hkey = ""
    hvalue = 0

    for key, value in a_dictionary.items():
        if value > hvalue:
            hvalue = value
            hkey = key
    return hkey
