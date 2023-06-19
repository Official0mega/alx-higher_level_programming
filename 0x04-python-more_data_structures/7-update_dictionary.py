#!/usr/bin/python3

"""
File_name: 7-update_dictionary.py
Created: 17th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x04-python-more_data_structures
Status: submitted.
"""


def update_dictionary(a_dictionary, key, value):

    """
    # Write a function that replaces or adds
    # key/value in a dictionary.
    # key argument will be always a strin
    # value argument will be any typ
    # If a key exists in the dictionary, the value will be replace
    # If a key doesn’t exist in the dictionary, it will be created
    # VARIABLE(" "):
    # update_dictionary(dict): Update dictionary
    """

    #  In this function, we first check if the given 'key'
    #  already exists in the 'a_dictionary'.
    #  if it does, we update the corresponding value with thr new 'value'.
    if key in a_dictionary:
        a_dictionary[key] = value

        #  if the 'key' doesn't exist, we add a new key / value pair to...
        #  ...the dictionary using the 'update()' method
    return a_dictionary


# Take for instance,
# a_dictionary = {'Language': "C", 'Number': 89, 'Track': "Low Level"}
#  update_dictionary(a_dictionary, "Language", Python)
#  print(a_dictionary)

#  or let's print another example
#  update_dictionary(a_dictionary, "ids",[1, 2, 4, 8, 16])
#  print(a_dictionary)
