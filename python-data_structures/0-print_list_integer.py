#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints each integer in a list on its own line using str.format().
    """
    for number in my_list:
        print("{}".format(number))
