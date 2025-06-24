#!/usr/bin/python3
"""
Module 2-matrix_divided
Divides all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divide each number in matrix by div.

    Args:
        matrix (list of lists of int/float): the data.
        div (int or float): non-zero divisor.

    Returns:
        list of lists of floats:
            each result rounded to 2 decimals.

    Raises:
        TypeError: for invalid types or row sizes.
        ZeroDivisionError: if div is zero.
    """
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix structure
    if (
        not isinstance(matrix, list)
        or not matrix
        or any(not isinstance(row, list) for row in matrix)
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check row sizes consistent
    size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) " "of integers/floats"
                )
            new_row.append(round(val / div, 2))
        new_matrix.append(new_row)

    return new_matrix
