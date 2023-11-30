#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 1
    if len(sys.argv) > 0:
        for word in sys.argv[1:]:
            print("{}: {}".format(count, word))
            count += 1
