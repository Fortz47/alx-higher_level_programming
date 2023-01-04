#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print('0{}'.format(i), end=", ")
    else:
        flag = ", " if i != 99 else '\n'
        print('{}'.format(i), end=flag)
