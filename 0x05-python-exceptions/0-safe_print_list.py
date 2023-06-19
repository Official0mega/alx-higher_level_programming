#!/usr/bin/python3

"""
File
_name: 0-safe_print_list.py
Created: 29th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x05-python-exceptions
Status: submitted.
"""


def safe_print_list(my_list=[], x=0):

    """
    # Write a function that prints x elements of a list.
    # my_list can contain any type (integer, string, etc.)
    # All elements must be printed on the same line followed by a new line.
    # x represents the number of elements to print
    # x can be bigger than the length of my_list
    # VARIABLE(" "):
    # safe_print_list(List): Safe list printing
    # Returns the real number of elements printed
    """
    count = 0
    try:
        """ The Try Block is to handle potential Errors that might Occur """
        """ initialized to keep track of the number of elements printed."""
        for count in range(x):
            print("{}".format(my_list[count]), end="")
            count += 1
        print("")
    except BaseException:
        print("")
    return count
    """ returns total elements as 'count' that was actually printed """
