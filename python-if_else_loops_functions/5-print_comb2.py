#!/usr/bin/python3

for i in range(100):  # Loop through numbers from 0 to 99
    if i != 99:
        print(f"{i:02}", end=", ")  # Print with leading zero if necessary
    else:
        print(f"{i:02}")  # Print the last number without a comma
