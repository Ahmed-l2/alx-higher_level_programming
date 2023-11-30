#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = 1
    if len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(count, argv[1]))
    elif len(argv) > 1:
        print("{} arguments:".format(len(argv) - 1))
        for word in argv[1:]:
            print("{}: {}".format(count, word))
            count += 1
    else:
        print("0 arguments.")
