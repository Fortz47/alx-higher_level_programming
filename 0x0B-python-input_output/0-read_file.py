#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """def read_file(filename="""
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        print(data, end='')
