#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific position."""

    lenght = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= lenght:
        return my_list
    else:
        my_list[idx] = element
        return my_list
