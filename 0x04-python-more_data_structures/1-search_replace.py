#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list and search < 0 and replace < 0:
        return None
    new_list = []
    for num in my_list:
        if num == search:
            new_list.append(replace)
        else:
            new_list.append(num)
    return new_list
