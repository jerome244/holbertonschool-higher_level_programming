#!/usr/bin/python3
"""
Module 2-matrix_divided

Provides matrix_divided(matrix, div) which divides all elements
of a matrix by div and returns a new matrix with each result
rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix (list of lists of int/float)
    by div and returns a new matrix.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of lists of floats: New matrix with each value rounded to 2 decimals.

    Raises:
        TypeError: If matrix is malformed or div is not a number.
        ZeroDivisionError: If div == 0.
    """
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix structure
    if (
        not isinstance(matrix, list)
        or len(matrix) == 0
        or any(not isinstance(row, list) for row in matrix)
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # All rows must be same size
    row_length = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            new_row.append(round(val / div, 2))
        new_matrix.append(new_row)

    return new_matrix
