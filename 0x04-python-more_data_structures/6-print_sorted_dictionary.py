#!/usr/bin/python3

"""
File_name: 6-print_sorted_dictionary.py
Created: 17th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x04-python-more_data_structures
Status: submitted.
"""


def print_sorted_dictionary(a_dictionary):

    """
    # Write a function that prints a dictionary by ordered keys.
    # You can assume that all keys are strings
    # Keys should be sorted by alphabetic orde
    # Only sort keys of the first level (don’t sort......
    # ....keys of a dictionary inside the main dictionary)
    # Dictionary values can have any type
    # VARIABLE(" "):
    # print_sorted_dictionary(dict): Print sorted dictionary
    """

    #  In this function, we first obtain a sorted list of keys using the.....
    #  .....'sorted()' function applied to the 'key()' method of the dictionary
    #  This ensures that the keys are sorted in alphabetical order.
    sorted_keys = sorted(a_dictionary.keys())

    #  We then iterate over the sorted keys and retrieve the...
    #  ...corresponding values from the dictionary
    for key in sorted_keys:
        key_values = a_dictionary[key]

        #  Finally, we print each key_values pair in the desired format.
        print(f"{key}: {key_values}")


#  Take for instance...
#  a_dictionary = {'Lang.': "C", 'Numb': 89, 'Track': "Low Lvl", 'ids': [1, 2]}
#  print_sorted_dictionary(a_dictionary)
