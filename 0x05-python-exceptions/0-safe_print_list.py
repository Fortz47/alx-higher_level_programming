#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    count = 0
    for i in range(x):
        count += 1
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            print("\n")
            return count - 1
    else:
        print("\n")
        return count
