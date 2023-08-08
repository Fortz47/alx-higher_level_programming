#!/usr/bin/python3

def remove_char_at(str, n):
    string = list()
    for i in range(len(str)):
        if i == n:
            continue
        string.append(str[i])

    return ''.join(string)
