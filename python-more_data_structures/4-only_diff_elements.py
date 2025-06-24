#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Returns a set of elements present in only one of the two input sets.

    Args:
        set_1 (set): First set of elements.
        set_2 (set): Second set of elements.

    Returns:
        set: A new set containing elements that are in set_1
        or set_2, but not both.
    """
    # Use symmetric difference to find elements unique to each set
    return set_1.symmetric_difference(set_2)
