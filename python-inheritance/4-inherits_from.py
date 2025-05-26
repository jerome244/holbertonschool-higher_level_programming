#!/usr/bin/python3
"""
This module defines the inherits_from function.

The function checks if an object is an instance of a subclass
of the specified class (not an instance of the class itself).
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, but not if obj is exactly a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj inherits from a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
