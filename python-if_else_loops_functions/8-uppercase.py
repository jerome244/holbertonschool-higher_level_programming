#!/usr/bin/python3


def uppercase(str):
    print("{}".format("".join(chr(ord(c) - 32) if "a" <= c <= "z" else c for c in str)))
