#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list and returns the sum.

    Args:
        my_list (list): List of integers.

    Returns:
        int: Sum of unique integers.
    """
    unique = set(my_list)
    total = 0
    for num in unique:
        total += num
    return total
