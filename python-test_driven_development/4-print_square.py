#!/usr/bin/python3
"""
Module 4-print_square

Provides a function to print a square of the `#` character.
"""


def print_square(size):
    """
    Prints a square with the character `#`.

    Args:
        size (int): the length of the square's sides.

    Raises:
        TypeError: if size is not an integer or is a float.
        ValueError: if size is < 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
