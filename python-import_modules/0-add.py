#!/usr/bin/python3
from add_0 import add  # Import the add function from add_0.py

a = 1  # Assign value 1 to a
b = 2  # Assign value 2 to b

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
