#!/usr/bin/python3

for i in range(10):  # First digit (0 to 9)
    for j in range(i + 1, 10):  # Second digit (greater than the first digit)
        if i != j:
            print(f"{i}{j}", end=", " if i < 8 or j < 9 else "\n")
