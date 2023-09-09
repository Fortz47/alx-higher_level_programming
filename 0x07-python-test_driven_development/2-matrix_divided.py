#!/usr/bin/python3
"""divides all element of a matrix"""


def matrix_divided(matrix, div):
    """divides all element of a matrix"""
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if isinstance(matrix, list) and len(matrix) != 0:
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(error)
        for row in matrix:
            if any(not isinstance(x, (int, float)) for x in row):
                raise TypeError(error)
            if any(type(x) is bool for x in row):
                raise TypeError(error)
        if not isinstance(div, (int, float)) or isinstance(div, bool):
            raise TypeError('div must be a number')
        if div == 0:
            raise ZeroDivisionError('division by zero')
    else:
        raise TypeError(error)
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return [[]]
    """if len(matrix) < 2:
        raise TypeError('Each row of the matrix must have the same size')"""
    x = len(matrix[0])
    if any(x != len(row) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    div = float(div)
    result = []
    for row in matrix:
        result.append(list(round(x / div, 2) for x in row))
    return result
