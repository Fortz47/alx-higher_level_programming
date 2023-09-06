#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters:
., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    tolist = list(text)
    line = ""
    for ch in tolist:
        line += ch
        if ch in '.:?':
            line += '\n\n'
            print(line.strip(' \t'), end='')
            line = ""
    print(line.strip(), end='')
