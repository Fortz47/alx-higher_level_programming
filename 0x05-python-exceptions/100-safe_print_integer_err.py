#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as ex:
        stderr.write(f"Exception: {ex}\n")
        return False
    else:
        return True
