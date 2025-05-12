#!/usr/bin/python3
"""
Module that defines a function to safely print elements of a list.
"""

def safe_print_list(my_list=[], x=0):
    """
    Prints up to x elements of my_list on the same line, then a new line.
    Returns the actual number of elements printed.
    Uses try/except to handle cases where x > len(my_list).
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except Exception:
            break
    print("")
    return count
