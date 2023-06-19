#!/usr/bin/python3

"""
File_name: 6-raise_exception_msg.py
Created: 29th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x05-python-exceptions
Status: submitted.
"""


def raise_exception_msg(message=""):

    """
    # Write a function that raises a name exception with a message.
    # VARIABLE(" "):
    # raise_exception_msg(NULL): Raise a message
    # You are not allowed to import any module
    # Return: Always 0. (Success)
    """
    """ In this function, we raise a 'NameError' exception with the provided
    ....'message'. if no message is provided, it will raise a 'NameError'
    ....without any specific message...."""
    raise NameError(message)
