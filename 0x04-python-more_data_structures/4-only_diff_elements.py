#!/usr/bin/python3

"""
File_name: 4-only_diff_elements.py
Created: 17th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x04-python-more_data_structures
Status: submitted.
"""


def only_diff_elements(set_1, set_2):

    """
    # Write a function that returns a set of all
    # elements present in only one set.
    # VARIABLE(" "):
    # only_diff_elements(set): Only differents
    """

    diff_set = set()

    #  This line will iterate over the elements in set_1
    for element in set_1:

        #  This will add the element to diff_set if it's not in set_2
        if element not in set_2:
            diff_set.add(element)

    #  will iterate over the element in set_2
    for element in set_2:

        #  it will then add the element to diff_set
        #  If it's not in set_1
        if element not in set_1:
            diff_set.add(element)

    return diff_set


#  Take for instance
#  set_1 = {"Python", "C", "Javascript"}
#  set_2 = {"Bash", "C", "Ruby", "Pearl"}
#  od_set = only_diff_elements(set_1, set_2)
#  print(od_set)
