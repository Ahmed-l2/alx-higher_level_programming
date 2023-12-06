#!/usr/bin/pythhon3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    new_list = set(my_list)
    result = reduce(lambda x, y: x + y, new_list)
