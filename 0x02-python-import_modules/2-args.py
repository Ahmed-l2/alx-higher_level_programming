#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 1
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            print("1 arugment:")
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
        for word in sys.argv[1:]:
            print("{}: {}".format(count, word))
            count += 1
    else:
        print("0 arguments.")
