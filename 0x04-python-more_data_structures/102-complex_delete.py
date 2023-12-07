#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    for akey, avalue in list(a_dictionary.items()):
        if avalue == value:
            del a_dictionary[akey]
    return a_dictionary
