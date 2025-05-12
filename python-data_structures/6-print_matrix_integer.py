#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    Each integer is printed with str.format(), separated by a space.
    After each row, prints a newline.
    If no matrix is provided, prints an empty line.

    Args:
        matrix (list of lists of int): The 2D list of integers to print.
    """
    for row in matrix:
        for idx, val in enumerate(row):
            end_char = " " if idx < len(row) - 1 else ""
            print("{}".format(val), end=end_char)
        print()
