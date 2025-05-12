#!/usr/bin/python3


def common_elements(set_1, set_2):
    """
    Returns a set of elements common to both input sets.

    Args:
        set_1 (set): First set of elements.
        set_2 (set): Second set of elements.

    Returns:
        set: A new set containing elements present in both set_1 and set_2.
    """
    # Use set intersection to find common elements
    return set_1.intersection(set_2)
