#!/usr/bin/python3

"""
File_name: 10-divisible_by_2.py
Created: 13th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def divisible_by_2(my_list=[]):

    """
    # This searches for multiples of 2:
    # Variables:
    # my_list(list): The first tuple..
    # Lists of Bool stating the possibility of division
    # of the number with 2 at same position in the List:
    """
    lists = []
    for num in my_list:
        if num % 2 == 0:
            lists.append(True)
        else:
            lists.append(False)
    return lists
