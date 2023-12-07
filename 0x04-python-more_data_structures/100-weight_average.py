#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    for tup in my_list:
        total += tup[0] * tup[1]
    sum_weight = sum(tup[1] for tup in my_list)
    total = total / sum_weight
    return total
