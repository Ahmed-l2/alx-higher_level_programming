#!/usr/bin/python3
for num in range(25, -1, -1):
    if num % 2 == 1:
        c = num + ord('a')
    else:
        c = num + ord('A')
    print("{}".format(chr(c)), end="")
