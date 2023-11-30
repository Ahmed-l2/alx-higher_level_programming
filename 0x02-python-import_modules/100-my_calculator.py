#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1

    if len(argv) == 4:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, a + b))
        elif argv[2] == "-":
            print("{} + {} = {}".format(a, b, a - b))
        elif argv[2] == "*":
            print("{} + {} = {}".format(a, b, a * b))
        elif argv[2] == "/":
            print("{} + {} = {}".format(a, b, a / b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
