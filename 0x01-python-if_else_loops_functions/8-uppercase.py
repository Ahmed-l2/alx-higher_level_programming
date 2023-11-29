#!/usr/bin/python3
def uppercase(str):
    results = ""
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            results += "{}".format(chr(ord(char) - 32))
        else:
            results += "{}".format(char)
        print("{}".format(results))
