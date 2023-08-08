#!/usr/bin/python3

for i in range(90, 64, -1):
    j = i
    if i % 2 == 0:
        j = j + 32
    print("{}".format(chr(j)), end='')
