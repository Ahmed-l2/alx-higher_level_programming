#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = []
    for num in my_list:
        if num % 2 == 0:
            boolist.append(True)
        else:
            boolist.append(False)
    return boolist
