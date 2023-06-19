#!/usr/bin/python3
"""Implementation of the 'add_attribute' function:
"""

'''
ile_Name: 101-add_attribute.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


def add_attribute(obj, attr_name, attr_value):
    """
    # Write a function that adds a new attribute to an...
    #....object if it’s possible
    # Raise a TypeError exception, with the message can't add....
    # new attribute if the object can’t have new attribute
    # VARIABLE(" "):
    # Attribute Adder(add_attribute): Can I?
    # Return: Always 0. (Success)
    """
    """
    The 'add_attribute' function takes three parameters: 'obj', 'attr_name'..
    and 'attr_value'. It first checks if the 'obj' has the '__dict__'
    attribute. if the '__dict__' attribute is not present, it means that..
    the object doesn't allow the addition of new attributes.
    In this case, the function raises a 'TypeError' with the message 'can't..
    add new attribute. If the '__dict__' attribute is present, the function
    uses the 'setattr()' function to add a new attribute with the specified
    'attr_name' and 'attr_value' to add the object.
    """
    if ('__dict__' in dir(obj)) and (type(obj.__dict__) is dict):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
