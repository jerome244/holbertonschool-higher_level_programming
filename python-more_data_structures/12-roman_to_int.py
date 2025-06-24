#!/usr/bin/python3


def roman_to_int(roman_string):
    """
    Converts a Roman numeral string to its integer value (1 to 3999).
    If input is not a valid string, returns 0.

    Args:
        roman_string (str): Roman numeral representation.

    Returns:
        int: Integer value or 0 on invalid input.
    """
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    # Mapping of Roman symbols to values
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in roman_string:
        curr = values.get(ch, 0)
        if curr == 0:
            return 0
        # If a smaller value precedes a larger one, subtract twice
        if prev < curr:
            total += curr - 2 * prev
        else:
            total += curr
        prev = curr
    return total
