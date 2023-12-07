#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    for tup in my_list:
        total += tup[0] * tup[1]
    total = total / (2 + 1 + 10 + 2)
    return total
