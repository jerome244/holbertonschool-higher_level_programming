#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """
    Returns a new list with all values of my_list multiplied by number using map.

    Args:
        my_list (list): List of numbers.
        number (int): The multiplier.

    Returns:
        list: New list with each original element multiplied by number.
    """
    return list(map(lambda x: x * number, my_list))
