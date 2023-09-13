#!/usr/bin/python3
"""appends a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""
    size = 0
    with open(filename, 'a', encoding='utf-8') as f:
        size = f.write(text)
    return size
