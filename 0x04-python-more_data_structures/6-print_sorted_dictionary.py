#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    sorted(a_dictionary)
    for k, v in a_dictionary.items():
        print("{:s}: {}".format(k, v))
