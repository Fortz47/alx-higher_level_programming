#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if argv.__len__() == 1:
        print("0 arguments.")
    elif argv.__len__() == 2:
        print("1 argument:")
        print(f"1: {argv[1]}")
    else:
        i = 0
        print(f"{len(argv) - 1} arguments:")
        for arg in argv[1:]:
            i += 1
            print(f"{i}: {arg}")
