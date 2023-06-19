#!/usr/bin/python3

"""
File_name: 2-safe_print_list_integers.py
Created: 29th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x05-python-exceptions
Status: submitted.
"""


def safe_print_list_integers(my_list=[], x=0):

    """
    # Function that prints the first x elements of a list and only integers.
    # my_list can contain any type (integer, string, etc.)
    # All integers have to be printed on the same line followed by a new line
    # other type of value in the list must be skipped (in silence).
    # x represents the number of elements to access in my_list
    # x can be bigger than the length of my_list...
    # ....if it’s the case, an exception is expected to occur
    # VARIABLE(" "):
    # safe_print_list(List): Print and count integers
    # Returns the real number of integers printed
    """
    real_numb = 0
    for y in range(x):
        items = my_list[y]
        """ iterating over each elements in 'my_list' using  a 'for' Loop"""
        try:
            """ Initializing a 'nested try block' within the 'for' Loop
            to handle exceptions and print only integers"""
            print("{:d}".format(my_list[y]), end="")
            real_numb += 1
        except (ValueError, TypeError):
            continue
    print("")
    return real_numb
