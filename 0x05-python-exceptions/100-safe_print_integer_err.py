#!/usr/bin/python3
import sys
"""
File_name: 100-safe_print_integer_err.py
Created: 29th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x05-python-exceptions
Status: submitted.
"""


def safe_print_integer_err(value):

    """
    # Write a function that prints an intege)
    # value can be any type (integer, string, etc.)
    # The integer should be printed followed by a new line
    # VARIABLE(" "):
    # Safe_print_integer(int): Safe integer print with error message
    # Returns:True if value has been correctly printed
    # Otherwise, False and prints in stderr the error precede by Exception:
    """
    try:
        """ use a 'try' block to attempt to format and
        print the value as an integer using """
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as error:
        """ If the formatting and printing are successful, we return True."""
        sys.stderr.write("Exception: {}\n".format(error))
        """ We then use sys.stderr.write to write the...
        error message to the standard error stream (sys.stderr)."""
        """" we return 'False' to indicate that an exception..."""
        """occurred during the printing proces."""
        return False
