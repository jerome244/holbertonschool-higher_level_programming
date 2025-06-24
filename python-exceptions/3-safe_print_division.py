#!/usr/bin/python3
"""
Module that defines a function to safely divide two
integers and print the result.
"""


def safe_print_division(a, b):
    """
    Divides two integers a and b, prints "Inside result:
    <result>" in a finally block,
    and returns the division result or None if division by zero occurred.
    Uses try/except/finally and "{}".format() for printing.
    """
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
