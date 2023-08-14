#!/usr/bin/python3

def no_c(my_string):
    str2list = list(my_string)
    for ch in str2list:
        if ch == 'c' or ch == 'C':
            str2list.remove(ch)
    return ''.join(str2list)
