#!/usr/bin/python3

"""
File_name: 5-no_c.py
Created: 13th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def no_c(my_string):

    """
    # Write a function that removes all characters c and C from a string.
    # VARIABLE(" "):
    # no_c(str) Can you C me now?
    # The function should return the new string
    """
    str_2 = []
    for list_alph in my_string:
        if list_alph not in 'cC':
            str_2.append(list_alph)
    return ''.join(str_2)
