#!/usr/bin/python3
"""
Module that defines a function to safely print an integer.
"""

def safe_print_integer(value):
    """
    Prints an integer value followed by a new line using "{:d}" formatting.
    Returns True if the value was successfully printed as an integer, else False.
    Uses try/except to handle non-integer inputs.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
