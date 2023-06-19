#!/usr/bin/python3
"""A function that inserts a line or text into a file after each line
containing a specific string.....
"""

'''
File_Naime: 100-append_after.py
Created Date: 13th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0B-python-input_output
Status: Submitted.
'''


def append_after(filename="", search_string="", new_string=""):
    """
    # Write a function that inserts a line of text to a file, after each
    # ...line containing a specific string (see example):
    # VARIABLE(" "):
    # Append After(filename,search,string): Search and update
    # Return: Always 0. (Success)
    """
    """
    This function 'append_after' takes three parameters: 'filename'(the name
    of the file), 'search_string' (the string to search for in each line)..
    and 'new_string'(the line of text to insert after each line containing..
    ...the search string.
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        """We read all the lines from the file using the 'readlines' method
        and store them in the 'lines' list.
        We also iterate over each line in the 'lines' list"""
        file.seek(0)
        """Using the 'seek' method with the offset parameter set to '0'"""
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
        """After iterating over all the lines, we use the 'truncate' method
        to remove any remaining content from the file beyond
        the current position.
        The line is automatically closed when the 'with' block is exited"""
