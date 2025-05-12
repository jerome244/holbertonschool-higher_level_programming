#!/usr/bin/python3
"""
Adds two integers.

The add_integer function adds two numbers after
casting floats to ints and checks types.
"""

def add_integer(a, b=98):
    """
    Adds two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
