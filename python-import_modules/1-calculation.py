#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10  # Assign value 10 to variable a
b = 5   # Assign value 5 to variable b

# Perform and print each of the calculations using the imported functions
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
