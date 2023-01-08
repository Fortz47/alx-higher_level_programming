#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """deletes the item at a specific position in a list."""

    lenght = len(my_list)
    new_list = list()
    j = 0
    if idx < 0 or idx >= lenght:
        return my_list
    del(my_list[idx])
    return my_list
