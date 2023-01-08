#!/usr/bin/python3

def no_c(my_string):
    """ removes all characters c and C from a string."""
    
    string2list = list(my_string)
    for i in string2list:
        if i == 'c' or i == 'C':
            string2list.remove(i)
    return ''.join(string2list)
