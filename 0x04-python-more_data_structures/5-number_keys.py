#!/usr/bin/python3

"""
File_name: 5-number_keys.py
Created: 17th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x04-python-more_data_structures
Status: submitted.
"""


def number_keys(a_dictionary):

    """
    # Write a function that returns the number of
    # keys in a dictionary.
    # VARIABLE(" "):
    # number_keys(dict): Number of keys
    """

    #  We will initialize a variable numb_of_keys to 0.
    numb_of_keys = 0

    #  Next, we will iterate over each key in the dictionary using a 'for' loop
    for key in a_dictionary:
        #  for each key we find, we'll increment the numb_of_keys by 1.
        numb_of_keys += 1

    #  Finally, we return the value of numb_of_keys which
    #  represents the number of keys in the dictionary
    return numb_of_keys


#  Take for instance
#  a_dictionary = {'language': "C", 'number': 13, 'track': "low level"}
#  nb_keys = number_keys(a_dictionary)
#  print(nb_keys)
