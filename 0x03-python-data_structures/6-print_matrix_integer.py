#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    k = 1
    for i in matrix:
        for j in i:
            if k < len(i):
                print("{}".format(j), end=' ')
            else:
                print("{}".format(j))
            k += 1
        k = 1
    if not i:
        print()
