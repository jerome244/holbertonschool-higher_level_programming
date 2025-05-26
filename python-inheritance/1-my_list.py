#!/usr/bin/python3
"""
Module that defines a MyList class to represent a list.
"""


class MyList(list):
    """
    Represent a list.
    """

    def print_sorted(self):
        """
        Print a sorted list
        """

        copy = self[:]
        copy.sort()

        print(copy)