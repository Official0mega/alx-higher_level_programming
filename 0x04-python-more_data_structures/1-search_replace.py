#!/usr/bin/python3

"""
File_name: 1-search_replace.py
Created: 17th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x04-python-more_data_structures
Status: submitted.
"""


def search_replace(my_list, search, replace):

    """
    # Write a function that replaces all occurrences
    # of an element by another in a new list.
    # VARIABLE(" "):
    # Search_replace(list): squared simple
    # my_list is the initial list
    # search is the element to replace in the list
    # replace is the new element
    """

    #  This line would create a new list
    #  to store the modified values
    sequel = []

    #  This line iterate over the elements in the original list
    for element in my_list:

        #  This line will check if the elements matches the search value
        if element == search:

            #  Then, if it matches, it will append
            #  the replaced value to the sequel list
            sequel.append(replace)
        else:

            #  If it doesn't match, it will then append,
            #  the original value to the sequel list
            sequel.append(element)
    #  This line will return the new list with replaced values
    return sequel


#  Take for an instance, (an example)
#  my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
#  search = 2
#  replace = 89

#  sequel = search_replace(my_list, search, replace)
#  print(sequel)
#  print(my_list)
