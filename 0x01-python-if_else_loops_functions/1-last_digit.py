#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
num = abs(number) % 10
if number < 0:
    num = num * -1
if num == 0:
    print(string, number, 'is', num, 'and is 0')
elif num < 6:
    print(string, number, 'is', num, 'and is less than 6 and not 0')
elif num > 5:
    print(string, number, 'is', num, 'and is greater than 5')
