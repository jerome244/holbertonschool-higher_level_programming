#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise, returning a new 2-integer tuple.

    If a tuple has fewer than 2 elements, missing values are treated as 0.
    If a tuple has more than 2 elements, only the first two are used.

    Args:
        tuple_a (tuple): First tuple of integers.
        tuple_b (tuple): Second tuple of integers.

    Returns:
        tuple: A new tuple (sum_first_elements, sum_second_elements).
    """
    # Get first elements or 0 if missing
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    # Get second elements or 0 if missing
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a0 + b0, a1 + b1)
