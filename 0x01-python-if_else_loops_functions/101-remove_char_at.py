#!/usr/bin/python3
def remove_char_at(str, n):
    num = 0
    for char in str:
        if num == n:
            print("", end="")
        else:
            print(char, end="")
        num += 1
