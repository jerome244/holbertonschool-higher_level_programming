#!/usr/bin/python3
"""
Module 3-say_my_name
Defines say_my_name(*args) to print names and handle missing args.
"""

def say_my_name(*args):
    """
    Print "My name is <first_name> <last_name>".

    Args:
        args[0] (str): first_name
        args[1] (str): last_name (optional)

    Raises:
        TypeError: if first_name or last_name not strings,
                  or if no arguments provided.
    """
    if len(args) == 0:
        raise TypeError(
            "say_my_name() missing 2 required positional arguments: "
            "'first_name' and 'last_name'"
        )

    first_name = args[0]
    last_name = args[1] if len(args) > 1 else ""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
