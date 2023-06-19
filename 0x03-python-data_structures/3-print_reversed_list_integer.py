#!/usr/bin/python3

"""
File_name: 3-print_reversed_list_integer.py
Created: 13th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def print_reversed_list_integer(my_list=[]):

    """
    # Write a function that prints all integers of a list, in reverse order.
    # VARIABLE(" "):
    # my_list(list) Print a list of integers... in reverse!
    # Format: one integer per line.
    # You have to use str.format() to print integers
    """
    if my_list:
        my_list.reverse()
        for rev in my_list:
            print("{:d}".format(rev))
