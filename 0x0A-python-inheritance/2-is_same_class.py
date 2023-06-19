#!/usr/bin/python3
"""function to check if the objects's type matches the specified class
"""

'''
File_Name: 2-is_same_class.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


def is_same_class(obj, a_class):
    """
    # Write a function that returns True if the object is exactly an instance
    # ....of the specified class ; otherwise False....
    # VARIABLE(" "):
    # Is Same Class(class/obj): Exact same object
    # Return: Always 0. (Success)
    """
    """
    In this code, '[type(obj)' returns the type of the 'obj' object....
    and 'a_class' is the specified class to check against.. The function....
    compares the object's type with the specified class using the 'is'
    ''''operator and returns 'True' if they match....
    Indicating that the object is object is exactly an instance of the...
    specified class.. Otherwise, it returns 'False'..."""
    return type(obj) is a_class
