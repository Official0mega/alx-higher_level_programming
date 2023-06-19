#!/usr/bin/python3

"""
File_name: 11-delete_at.py
Created: 13th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def delete_at(my_list=[], idx=0):
    if my_list:
        if 0 <= idx < len(my_list):
            del my_list[idx]
    return my_list
