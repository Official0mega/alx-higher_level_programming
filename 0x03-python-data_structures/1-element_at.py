#!/usr/bin/python3

"""
File_name: 1-element_at.py
Created: 12th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None

    return my_list[idx]

    my_list = [1, 2, 3, 4, 5]

    indices = my_list[3]
    idx = 3
    print("Element at index {:d} is {} ".format(idx, indices))
