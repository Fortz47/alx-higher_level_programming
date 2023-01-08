#!/usr/bin/python3

def no_c(my_string):
    """ removes all characters c and C from a string."""

    string2list = list(my_string)
    j = 0
    for i in string2list:
        if i == 'c' or i == 'C'
        del(string2list[j])
        j += 1

    list2String = ''.join(string2list)
    return list2String
