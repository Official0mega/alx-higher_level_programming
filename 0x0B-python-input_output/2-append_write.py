#!/usr/bin/python3
"""Function that appends a string to the end of a text file and returns the...
.....number of characters added...
"""

'''
File_Naime: 2-append_write.py
Created Date: 13th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0B-python-input_output
Status: Submitted.
'''


def append_write(filename="", text=""):
    """
    # Write a function that appends a string at the end of a text file (UTF8)
    # and returns the number of characters added:....
    # You must use the with statement
    # VARIABLE(" "):
    # Append Write(filename, text): Append to a file
    # Return: Always 0. (Success)
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        """'append_write' function is defined with two optional parameter
        'filename' represents the name of the file to append, while 'text'...
        ...represents the string to be appended to the file.
        If no filename or text is provided,it defaults to an empty strings."""
        chars_added = file.write(text)
        return chars_added
        """Finally, the function returns the value of 'chars_added'...
        .....which represents the number of characters added to the file"""
