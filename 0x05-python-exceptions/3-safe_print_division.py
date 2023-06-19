#!/usr/bin/python3

"""
File_name: 3-safe_print_division.py
Created: 29th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x05-python-exceptions
Status: submitted.
"""


def safe_print_division(a, b):

    """
    # Write a function that divides 2 integers and prints the result.
    # The result of the division should print on the finally:...
    # ...section preceded by Inside result:
    # You have to use try: / except: / finally:
    # VARIABLE(" "):
    # safe_print_division(List): Integers division with debug
    # Return: the value of the division, otherwise: None
    """
    try:
        """The try block attempts to perform the division a / b."""
        result = a / b
    except ZeroDivisionError:
        """If a ZeroDivisionError occurs (i.e., division by zero),
        the except, block sets the result to None."""
        result = None
    finally:
        print("Inside result: {}".format(result))
        """The finally block always executes, and it prints the result..
        ...using the print statement with the desired format."""
        return result
