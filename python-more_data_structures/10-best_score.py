#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Returns the key with the highest integer value in a dictionary.

    Args:
        a_dictionary (dict): Dictionary with string keys and integer values.

    Returns:
        str: The key corresponding to the highest value, or None if
        the dictionary is None or empty.
    """
    if not a_dictionary:
        return None

    best = None
    max_value = None
    for key, value in a_dictionary.items():
        if max_value is None or value > max_value:
            max_value = value
            best = key
    return best
