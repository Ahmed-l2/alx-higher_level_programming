#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) == 4:
        a = int(argv[1])
        b = int(argv[3])
        sign = argv[2]
        if sign == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sign == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sign == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif sign == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
