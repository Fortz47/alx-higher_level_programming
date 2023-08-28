#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while x:
            print(f'{my_list[i]}', end='')
            i += 1
            x -= 1
    except IndexError as err:
        print()
        return i
    else:
        print()
        return i
