#!/usr/bin/python3
for num in range(10):
    for num1 in range(10):
        if num1 > num:
            if num < 8:
                print("{}{}".format(num, num1), end=", ")
            else:
                print("{}{}".format(num, num1))
