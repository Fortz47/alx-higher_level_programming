#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers."""

    for i in matrix:
        k = 1
        for j in i:
            flag = " " if k < len(i) else '\n'
            print("{:d}".format(j), end=flag)
            k += 1
