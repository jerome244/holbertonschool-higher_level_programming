#!/usr/bin/python3
"""Defines a text_indentation function."""


def text_indentation(text):
    """
    prints text formatted with two newlines after . ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new = text.split(".")
    new = [line.strip() for line in new]
    new = [
        (line + ".\n\n") if index + 1 != len(new) else line
        for index, line in enumerate(new)
    ]
    new = "".join(new)
    new = new.split(":")
    new = [line.strip(" ") for line in new]
    new = [
        (line + ":\n\n") if index + 1 != len(new) else line
        for index, line in enumerate(new)
    ]
    new = "".join(new)
    new = new.split("?")
    new = [line.strip(" ") for line in new]
    new = [
        (line + "?\n\n") if index + 1 != len(new) else line
        for index, line in enumerate(new)
    ]
    new = "".join(new)
    print("{:s}".format(new), end="")
