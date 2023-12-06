#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    new_list = set(my_list)
    result = 0
    for num in new_list:
        result += num
    return result
