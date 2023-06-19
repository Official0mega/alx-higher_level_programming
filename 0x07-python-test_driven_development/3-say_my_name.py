#!/usr/bin/python3
""" Say_My_Name function
"""

'''
File_name: 3-say_my_name.py
Created: 3rd of June, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x07-python-test_driven_development
Status: submitted.
'''


def say_my_name(first_name, last_name=""):

    """
    # Write a function that prints My name is <first name> <last name>
    # first_name and last_name must be strings otherwise, raise a....
    # ....TypeError exception with the message
    # first_name must be a string or last_name must be a string....
    # VARIABLE(" "):
    # Say My Name(Str): Say my name
    # Return: Always 0, (Success).

    Prints the name in the format 'My name is <first name> <last name>'.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to.''.

    Raises:
        None
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
