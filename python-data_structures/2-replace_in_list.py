#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replaces the element at index `idx` in `my_list` with `element`.
    If `idx` is negative or out of range, the list is left unchanged.
    Returns the list (modified or original).
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
