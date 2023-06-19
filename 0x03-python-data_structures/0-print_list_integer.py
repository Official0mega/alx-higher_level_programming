#!/usr/bin/python3

"""
File_name: 0-print_list_integer.py
Created: 13th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def print_list_integer(my_list=[]):

    """
    # Write a function that prints all integers of a list.
    # Format: one integer per line. See example
    # VARIABLE(" "):
    # my_list(list)  Print a list of integers
    # You are not allowed to cast integers into strings
    # You have to use str.format() to print integers
    """
    for integers in my_list:
        print("{:d}".format(integers))
