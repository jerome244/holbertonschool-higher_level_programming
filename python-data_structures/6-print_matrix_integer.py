#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, val in enumerate(row):
            end_char = " " if idx < len(row) - 1 else ""
            print("{}".format(val), end=end_char)
        print()
