#!/usr/bin/python3


def max_integer(my_list=[]):
    """
    Finds the biggest integer in a list.
    If the list is empty, returns None.

    Args:
        my_list (list): List of integers.

    Returns:
        int or None: The biggest integer or None if the list is empty.
    """
    if len(my_list) == 0:
        return None
    max_val = my_list[0]
    for num in my_list[1:]:
        if num > max_val:
            max_val = num
    return max_val
