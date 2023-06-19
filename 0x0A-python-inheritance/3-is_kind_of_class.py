#!/usr/bin/python3
"""function to check if the objects is an instance of a class that inherited
from  the specified class.....
"""

'''
File_Name: 3-is_kind_of_class.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


def is_kind_of_class(obj, a_class):
    """
    # Write a function that returns True if the object is an instance of, or
    # if the object is an instance of a class that inherited from,
    # the specified class ; otherwise False....
    # VARIABLE(" "):
    # Is Kind of Class(class/obj): Same class or inherit from
    # Return: True if successful Otherwise, it returns False.
    """
    """
    In this code, 'isinstance(obj), a_class)' checks if 'obj' is an instance
    ...of 'a_class' or if 'obj' is an instance of a class tjay inherited from
    ..'a_class'. The function returns 'True' if the check is successful,
    indicating that the object is either an instance of the specified class...
    ...or an inherited class...
    otherwise, it returns 'False'"""
    return isinstance(obj, a_class)
