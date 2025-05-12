#!/usr/bin/python3
"""
Module that defines a function which raises a NameError with a custom message.
"""

def raise_exception_msg(message=""):
    """
    Raises a NameError with the provided message.
    """
    raise NameError(message)
