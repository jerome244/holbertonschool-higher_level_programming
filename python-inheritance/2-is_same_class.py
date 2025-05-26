#!/usr/bin/python3
"""
This module defines the is_same_class function.

The function returns True if the object is exactly an instance
of the specified class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
