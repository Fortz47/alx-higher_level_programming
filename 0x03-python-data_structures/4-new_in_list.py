#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """function that replaces an element in a list at a
    specific position without modifying the original list"""

    new = list.copy(my_list)
    lenght = len(my_list)
    if idx < 0:
        return new
    elif idx >= lenght:
        return new
    else:
        new[idx] = element
        return new
