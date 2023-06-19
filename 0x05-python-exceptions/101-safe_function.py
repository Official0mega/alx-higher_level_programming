#!/usr/bin/python3
import sys

"""
File_name: 101-safe_function.py
Created: 29th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x05-python-exceptions
Status: submitted.
"""


def safe_function(fct, *args):

    """
    # Write a function that executes a function safely.
    # VARIABLE(" "):
    # mafic_calculation(int): ByteCode -> Python #4
    # Returns: the result of the function,
    # Otherwise, returns None if something happens during the...
    # ....function and prints in stderr the error precede by Exception:
    """
    try:
        """We use a 'try'-except' block to execute the provided function 'fct'
        with the given arguments '*args'."""
        total_sum = fct(*args)
        """If the function execution is successful, total_sum is returned"""
        return total_sum
    except Exception as error:
        """The error message is printed out using the below function"""
        sys.stderr.write("Exception: {}\n".format(error))
        """ returns None to indicate something went wrong......
        .......during the execution"""
        return None
