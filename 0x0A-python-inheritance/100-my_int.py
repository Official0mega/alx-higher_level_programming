#!/usr/bin/python3
"""Implementation of the 'MyInt' class that inherits from 'int'
"""

'''
ile_Name: 100-my_int.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


class MyInt(int):
    """
    # Write a class MyInt that inherits from int:
    # VARIABLE(" "):
    # MYInt(int): My integer
    # MyInt is a rebel. MyInt has == and != operators inverted
    # Return: Always 0. (Success)
    """
    """
    The 'MyInt' classs inherits from the built-in 'int' class. It overrides
    the '__eq__' and '__ne_' methods to invert the behavior of the '==' and
    '!=' operators, respectively. The overridden methods call the corres...
    ..ponding methods of the 'int' class using the 'super()' function and...
    then return the inverse of the result"""
    def __eq__(self, other):
        """
        The method to check if the given value is not equal to the object"""
        return super().__ne__(other)

    def __ne__(self, other):
        """
        The method to check if the given value is equal to the object"""
        return super().__eq__(other)
