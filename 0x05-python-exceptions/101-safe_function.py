#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (ZeroDivisionError, IndexError, TypeError) as err:
        stderr.write(f"Exception: {err}\n")
        return None
    else:
        return result
