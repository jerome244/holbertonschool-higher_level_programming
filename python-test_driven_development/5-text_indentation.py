#!/usr/bin/python3
"""
Module 5-text_indentation

Provides function text_indentation that prints text with two new lines
after each '.', '?', and ':' character, without leading/trailing spaces.
"""

def text_indentation(text):
    """
    Prints text with two new lines after '.', '?', and ':' characters.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: if text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    separators = '.?:'
    i = 0
    length = len(text)

    while i < length:
        char = text[i]
        print(char, end="")
        if char in separators:
            # skip following spaces
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            print("\n")
            continue
        i += 1
