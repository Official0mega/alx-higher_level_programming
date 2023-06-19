#!/usr/bin/python3

"""
File_name: 1-safe_print_integer.py
Created: 29th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x05-python-exceptions
Status: submitted.
"""


def safe_print_integer(value):

    """
    # Write a function that prints an integer with "{:d}".format().
    # value can be any type (integer, string, etc.)
    # The integer should be printed followed by a new line
    # VARIABLE(" "):
    # Safe_print_integer(int): Safe Printing of an integers list
    # Return: True if value has been correctly printed(int)
    """
    try:
        """ 'try' This would attempt to convert the 'value to an Integer """
        print("{:d}".format(value))
        """ We formatted the integer using '{:d}.format()' """
        return True
    except (ValueError, TypeError):
        """ We would return 'True' if the value is successfully printed
    as an Integer """
        """ if there's any error during the conversion or formatting,
        we would catch 'ValueError' or 'TypeError' exception respectively """
        return False
        """ We would return 'False' to indicate the value couldn't
    be printed as an Integer """
