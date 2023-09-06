#!/usr/bin/python3
"""prints a square with character #"""


def print_square(size):
    """prints a square with character #"""
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    result = list("#" * size for i in range(size))
    print('\n'.join(result))
