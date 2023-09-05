#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """Function that adds two integers"""
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, bool):
        raise TypeError('a must be an integer')
    if isinstance(b, bool):
        raise TypeError('b must be an integer')
    return a + b
