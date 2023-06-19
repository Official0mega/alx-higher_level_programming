#!/usr/bin/python3
""" print_square function
"""

'''
File_name: 4-print_square.py
Created: 3rd of June, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x07-python-test_driven_development
Status: submitted.
'''


def print_square(size):

    """
    # Write a function that prints a square with the character #.
    # size is the size length of the square......
    # size must be an integer, otherwise raise a TypeError,,,,,,
    # exception with the message size must be an integer.......
    # if size is less than 0, raise a ValueError exception with the....
    # .....message size must be >= 0
    # f size is a float and is less than 0, raise a TypeError....
    # ....exception with the message size must be an integer......
    # VARIABLE(" "):
    # Print Square(Str): Print Square
    # Return: Always 0, (Success).

    Prints a square with the character '#' of the given size.

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer...
        alueError: If size is less than 0.

    Example:
        print_square(3)
        # Output:
        # ###
        # ###
        # ###

        print_square(5)
        # Output:
        # #####
        # #####
        # #####
        # #####
        # #####
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
        return
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
