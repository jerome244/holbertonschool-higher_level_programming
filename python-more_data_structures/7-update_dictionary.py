#!/usr/bin/python3



def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value in the given dictionary.

    If the key already exists in the dictionary, its value is replaced.
    If the key does not exist, a new key/value pair is added.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to replace or add.
        value: The value to assign to the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
