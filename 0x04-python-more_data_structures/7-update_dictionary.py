#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """ replaces or adds key/value in a dictionary."""

    for k, v in a_dictionary.items():
        if k not in a_dictionary:
            a_dictionary[key] = value
        else:
            a_dictionary[k] = value
