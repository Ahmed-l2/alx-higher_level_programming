#!/usr/bin/python3
def uppercase(str):
    i = 0
    for num in range(97, 123):
        if ord(str[i]) == num:
            print("{}".format(chr(num + 33))
        else:
            print("{}".format(str[i]))
        i += 1
