#!/usr/bin/python3

for i in range(122, 96, -1):  # Start from 'z' (122) and go down to 'a' (97)
    if (122 - i) % 2 == 0:
        print(chr(i), end="")  # Print lowercase
    else:
        print(chr(i - 32), end="")
