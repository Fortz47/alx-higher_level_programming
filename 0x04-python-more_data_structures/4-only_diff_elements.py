#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """returns a set of all elements present in only one set."""
    return (set_1.difference(set_2)).union(set_2.difference(set_1))
