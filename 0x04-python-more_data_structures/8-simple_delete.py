#!/usr/bin/python3

"""
File_name: 8-simple_delete.py
Created: 17th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x04-python-more_data_structures
Status: submitted.
"""


def simple_delete(a_dictionary, key=""):

    """
    # Write a function that deletes a key in a dictionary.
    # key argument will be always a string
    # If a key doesn’t exist, the dictionary won’t change
    # VARIABLE(" "):
    # simple_delete(dict): Simple delete by key
    """

    #  in this function, we will check if the given 'key' exists in the...
    #  ...'a_dictionary' using the 'in' operator
    if key in a_dictionary:

        #  If the key exists, we will use the 'del' statement to delete...
        #  ...the key-value pair from the dictionary
        del a_dictionary[key]
    return a_dictionary
