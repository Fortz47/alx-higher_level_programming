#!/usr/bin/python3
if __name__ == "__main__":
    """prints the result of the addition of all arguments."""
from sys import argv

sum = 0
if len(argv) == 1:
    sum = 0
else:
    for i in argv[1:]:
        sum += int(i)
print(f"{sum}")
