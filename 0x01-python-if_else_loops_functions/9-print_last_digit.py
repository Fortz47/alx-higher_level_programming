#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number *= -1

    num = number % 10
    print(f'{num}', end="")
    return num
