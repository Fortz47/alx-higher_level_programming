#!/usr/bin/python3

def max_integer(my_list=[]):
    """finds the biggest integer of a list."""

    if my_list == []:
        return None
    lenght = len(my_list)
    j = 0

    for i in range(lenght):
        if my_list[j] >= my_list[i]:
            continue
        else:
            j = i
    return my_list[j]
