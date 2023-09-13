#!/usr/bin/python3
"""writes a string to a text file (UTF8) and
returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written"""
    size = 0
    with open(filename, 'w', encoding='utf-8') as f:
        size = f.write(text)
    return size
