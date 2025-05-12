#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at index `idx` from `my_list` in place.
    If `idx` is negative or out of range, the list is unchanged.

    Args:
        my_list (list): The list of elements.
        idx (int): The index of the element to delete.

    Returns:
        list: The modified list (or original if `idx` invalid).
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Remove element without using pop()
    del my_list[idx]
    return my_list
