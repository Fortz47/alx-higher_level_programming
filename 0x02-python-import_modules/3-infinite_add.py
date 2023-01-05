#!/usr/bin/python3
from sys import argv

sum = 0
if len(argv) == 1:
    sum = 0
else:
    for i in argv[1:]:
        sum += int(i)
print(f"{sum}")
