#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    return ([list(map(lambda y: y * y, row)) for row in matrix])
