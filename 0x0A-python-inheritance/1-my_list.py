#!/usr/bin/python3
"""We can inherit from the built-in 'list' class and add a 'print_sorted...
"""

'''
File_Name: 1-my_list.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


class MyList(list):
    """
    # Write a class MyList that inherits from list:
    # Public instance method: def print_sorted(self): that prints...
    # ....the list, but sorted (ascending sort).
    # VARIABLE(" "):
    # My List(self): My list
    # Return: Always 0. (Success)
    """
    """ In this code, 'MyList' inherits from 'list' class. The 'print_sorted'
    method sorts the list using the  'sorted' function and then....
    ...prints the sorted list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
