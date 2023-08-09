#!/usr/bin/python3

def uppercase(str):
    strUpper = list()
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            upper = chr(ord(str[i]) - 32)
            strUpper.append(upper)
        else:
            strUpper.append(str[i])
    print("{}".format(''.join(strUpper)))
