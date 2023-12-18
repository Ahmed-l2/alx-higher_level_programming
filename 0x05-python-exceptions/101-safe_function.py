#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
