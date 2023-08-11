#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if argv.__len__() == 1:
        print("0")
    elif argv.__len__() == 2:
        print(f"{int(argv[1])}")
    else:
        i = 1
        _sum = 0
        for arg in argv[1:]:
            _sum += int(argv[i])
            i += 1
        print(f"{_sum}")
