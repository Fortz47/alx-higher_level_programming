#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an intger and returns True
    if value is an integer or False if value is 
    not an integer

    """

    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
