#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    tuple_new = ()
    add_1 = (0 if len(tuple_a) < 2 or tuple_a[0] < 0 else tuple_a[0]) +\
            (0 if len(tuple_b) < 2 or tuple_b[0] < 0 else tuple_b[0])
    add_2 = (0 if len(tuple_a) < 2 or tuple_a[1] < 0 else tuple_a[1]) +\
            (0 if len(tuple_b) < 2 or tuple_b[1] < 0 else tuple_b[1])
    tuple_new = (add_1, add_2)
    return tuple_new
