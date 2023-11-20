#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    x = None
    try:
        x = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
    return x
