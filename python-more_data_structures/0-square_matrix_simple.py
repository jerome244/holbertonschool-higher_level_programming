#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Returns a new matrix with each value squared from the input matrix.
    """
    return [[value * value for value in row] for row in matrix]
