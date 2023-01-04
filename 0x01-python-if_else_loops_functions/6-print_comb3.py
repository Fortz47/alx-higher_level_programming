#!/usr/bin/python3
for i in range(10):
    for k in range(10):
        if i == 8 and k == 9:
            print("{}{}".format(i, k), end="\n")
        if i != k and k > i and i != 8 and k != 9:
            print("{}{}".format(i, k), end=", ")
