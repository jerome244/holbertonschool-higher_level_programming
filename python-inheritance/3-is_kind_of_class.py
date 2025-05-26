#!/usr/bin/python3
"""
This module defines the is_kind_of_class function.

The function checks if an object is an instance of,
or inherits from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or if the object is an instance
    of a class that inherited from, the specified class. Otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is instance or inherits from a_class, else False.
    """
    return isinstance(obj, a_class)
