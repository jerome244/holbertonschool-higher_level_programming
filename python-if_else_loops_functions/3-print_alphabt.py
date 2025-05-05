#!/usr/bin/python3

for i in range(97, 123):  # ASCII values of 'a' to 'z' are 97 to 122
    if chr(i) != 'q' and chr(i) != 'e':  # Exclude 'q' and 'e'
        print(chr(i), end="")
