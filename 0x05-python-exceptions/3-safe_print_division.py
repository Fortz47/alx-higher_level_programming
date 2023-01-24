#!/usr/bin/python3

def safe_print_division(a, b):
    """divides two integers"""

    try:
        c = a / b
    except ZeroDivisionError:
        c = 'None'
    finally:
        print("Inside result: {}".format(c))
