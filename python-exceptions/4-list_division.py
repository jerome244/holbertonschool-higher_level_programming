#!/usr/bin/python3
"""
Module that defines a function to divide element by element two lists safely.
"""

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element my_list_1 and my_list_2 up to list_length.
    Returns a new list of length list_length with the results.

    If an element index is out of range for either list:
        prints "out of range" and appends 0 to the result list.
    For non-integer/float elements:
        prints "wrong type" and appends 0.
    For division by zero:
        prints "division by 0" and appends 0.
    Uses try/except/finally structure and no imports.
    """
    result = []
    for i in range(list_length):
        try:
            num = my_list_1[i]
            den = my_list_2[i]
        except Exception:
            print("out of range")
            result.append(0)
            continue
        try:
            res = num / den
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except Exception:
            print("wrong type")
            res = 0
        finally:
            result.append(res)
    return result
