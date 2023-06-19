#!/usr/bin/python3

"""
File_name: 8-multiple_returns.py
Created: 13th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def multiple_returns(sentence):

    """
    # Write a function that returns a tuple with
    # the length of a string and its first character.
    # VARIABLE(" "):
    # sentence(str): The first tuple..
    # If the sentence is empty,
    # the first character should be equal to None
    """
    length = len(sentence)
    if length == 0:
        str_len = None
        first_tuple = (length, str_len)
        return first_tuple
    else:
        str_len = sentence[0]
        first_tuple = (length, str_len)
        return first_tuple
