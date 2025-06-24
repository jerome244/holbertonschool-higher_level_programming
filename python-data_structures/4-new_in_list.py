#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Returns a new list with `element` at position `idx`.
    If `idx` is negative or out of range, returns a copy of the original list.

    Args:
        my_list (list): The original list of integers.
        idx (int): The index at which to replace the element.
        element: The new element to insert.

    Returns:
        list: A new list with the replacement or a copy of the original.
    """
    # If idx is invalid, return a shallow copy of the list
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    # Make a shallow copy and replace the element
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
