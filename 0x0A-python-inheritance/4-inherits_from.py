#!/usr/bin/python3
"""function to check if the object's class is a subclass (directly or ....
....indirectly) of the specified class...
"""

'''
File_Name: 4-inherits_from.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


def inherits_from(obj, a_class):
    """
    # Write a function that returns True if the object is an instance of a
    # class that inherited (directly or indirectly) from the specified class;
    # .........otherwise False.......
    # VARIABLE(" "):
    # Inherits From(class/obj): Only sub class of
    # Return: True if successful Otherwise, it returns False.
    """
    """
    In this code, 'isinstance(obj), a_class)' checks if the type of 'obj'...
    ....is a subclass of 'a_class'. The condition 'type(obj) != a_class...
    ensures that the object's class is not tje same as the specified class...
    ...The function returns 'True if the check is successful, indicating that
    the object is an inheritance of a class that inherited(directly or...
    indirectly) from the specified...
    ...class..Otherwise, it returns 'False'."""
    return isinstance(obj, a_class) and type(obj) != a_class
