#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    my_list.sort()
    return my_list[-1]
