#!/usr/bin/python3
def uppercase(str):
    string = []
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            string.append(chr(ord(i) - 32))
        else:
            string.append(i)
    String = ''.join(string)
    print('{}'.format(String))
