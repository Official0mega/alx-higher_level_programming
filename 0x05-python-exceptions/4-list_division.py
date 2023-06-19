#!/usr/bin/python3

"""
File_name: 6-raise_exception_msg.py
Created: 29th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x05-python-exceptions
Status: submitted.
"""


def list_division(my_list_1, my_list_2, list_length):

    """
    # Write a function that divides element by element 2 lists.
    # my_list_1 and my_list_2 can contain any type (integer, string, etc.)
    # list_length can be bigger than the length of both lists
    # VARIABLE(" "):
    # list_division(List): Divide a List
    # You are not allowed to import any module
    # Return: a new list (length = list_length) with all divisions
    """
    my_list = []
    for x in range(list_length):
        """ In this function, we iterate over the range of 'List_Length'...
        ...and perform element-wise division on the corresponding elements...
        ...from 'my_list_1' and 'my_list_2' respectively..."""
        try:
            total_sum = 0
            if x < len(my_list_1) and x < len(my_list_2):
                numb1 = my_list_1[x]
                numb2 = my_list_2[x]
                total_sum = numb1 / numb2
            else:
                raise IndexError("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            my_list.append(total_sum)
    return my_list
