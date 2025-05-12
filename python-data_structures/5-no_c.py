#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all characters 'c' and 'C' from the input string.

    Args:
        my_string (str): The original string.

    Returns:
        str: A new string with 'c' and 'C' characters removed.
    """
    new_str = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_str += ch
    return new_str
