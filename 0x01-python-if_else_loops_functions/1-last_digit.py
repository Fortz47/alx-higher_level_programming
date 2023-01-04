#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number *= -1
    remainder = number % 10
    remainder *= -1
    print(f"Last digit of -{number} is {remainder}", end=" ")
else:
    remainder = number % 10
    print(f"Last digit of {number} is {remainder}", end=" ")

if remainder > 5:
    print('and is greater than 5')
elif remainder == 0:
    print('and is 0')
elif remainder < 6 and remainder != 0:
    print('and is less than 6 and not 0')
