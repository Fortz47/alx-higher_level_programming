#!/usr/bin/python3

if __name__ == "__main__":
    """ prints the number of and the list of its arguments."""

    from sys import argv

    lenght = len(argv)
    k = 1
    if lenght == 1:
        print("0 arguments.")
    elif lenght == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(lenght - 1))
        for i in argv[1:]:
            print("{}: {}".format(k, i))
            k += 1
