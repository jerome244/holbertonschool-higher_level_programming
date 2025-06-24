#!/usr/bin/python3
"""Multiply all elements of a list by a number using map."""

def multiply_list_map(my_list=[], number=0): return list(map(lambda x: x * number, my_list))
