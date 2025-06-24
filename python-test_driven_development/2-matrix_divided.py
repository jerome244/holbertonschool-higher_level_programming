#!/usr/bin/python3
"""
Module 2-matrix_divided
Divides all elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divide each number in matrix by div.

    Args:
        matrix (list of lists of int/float): data to process.
        div (int or float): divisor (not zero).

    Returns:
        list of lists of floats:
            each result rounded to 2 decimals.

    Raises:
        TypeError: for invalid types or sizes.
        ZeroDivisionError: if div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a non-empty list of lists"
        )

    size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a list of lists"
            )
        if len(row) != size:
            raise TypeError(
                "each row must have same size"
            )
        new_row = []
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(
                    "matrix must contain only numbers"
                )
            new_row.append(round(val / div, 2))
        new_matrix.append(new_row)

    return new_matrix
