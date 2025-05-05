#!/usr/bin/python3
import sys


def main():
    # Starting sum as 0
    total = 0

    # Loop through all arguments (starting from index 1 to skip the script name)
    for arg in sys.argv[1:]:
        total += int(arg)  # Convert each argument to integer and add to total

    print(total)  # Print the result


if __name__ == "__main__":
    main()
