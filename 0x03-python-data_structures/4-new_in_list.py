#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    for item in my_list:
        copy.append(item)
    if idx < 0:
        return copy
    elif idx > len(my_list) - 1:
        return copy
    else:
        copy[idx] = element
        return copy
