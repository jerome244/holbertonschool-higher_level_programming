#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Prints the contents of a dictionary sorted by key (first-level only).

    Args:
        a_dictionary (dict): The dictionary to print.

    Returns:
        None
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
