#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    Returns a list of booleans indicating
    if each integer in `my_list` is a multiple of 2.

    Args:
        my_list (list): List of integers.

    Returns:
        list: A new list of True/False values, same
        length as `my_list`.
    """
    result = []
    for num in my_list:
        # True if num is divisible by 2, False otherwise
        result.append(num % 2 == 0)
    return result
