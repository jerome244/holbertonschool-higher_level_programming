#!/usr/bin/python3
"""
Module that defines a function to safely print the
first x integer elements of a list.
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of my_list that are integers,
    all on the same line,
    followed by a new line.
    Non-integer elements are skipped silently.
    If x is greater than the list length, stops when the list ends.
    Returns the real number of integers printed.
    Uses try/except to handle out-of-range indices and non-integers.
    """
    count = 0
    for i in range(x):
        try:
            value = my_list[i]
        except Exception:
            # IndexError or other: stop iteration
            break
        try:
            # Attempt to print as integer
            print("{:d}".format(value), end="")
            count += 1
        except Exception:
            # ValueError, TypeError for non-integer: skip silently
            continue
    print("")
    return count
