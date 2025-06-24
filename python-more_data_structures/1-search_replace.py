#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    Returns a new list where all occurrences of 'search'
    in my_list are replaced by 'replace'.

    Args:
        my_list (list): The original list.
        search: The element to search for.
        replace: The element to replace with.

    Returns:
        list: A new list with replacements.
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
