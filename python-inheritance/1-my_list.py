#!/usr/bin/python3
"""
This module defines the MyList class.

MyList inherits from list and has a method print_sorted
that prints the list in ascending order.
"""


class MyList(list):
    """
    MyList class that inherits from list.

    It includes a method to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order (does not modify the list).
        """
        print(sorted(self))
