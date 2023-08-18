#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_ = 0
    for k, v in a_dictionary.items():
        if v >= max_:
            max_ = v
            max_key = k
    return max_key
