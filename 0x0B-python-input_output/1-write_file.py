#!/usr/bin/python3
"""Function that writes a string to a text file and returns the number...
.....of characters written:...
"""

'''
File_Naime: 1-write_file.py
Created Date: 13th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0B-python-input_output
Status: Submitted.
'''


def write_file(filename="", text=""):
    """
    # Write a function that writes a string to a text file (UTF8) and returns
    # the number of characters written:
    # You must use the with statement
    # VARIABLE(" "):
    # Write File(filename): Write to a file
    # Return: Always 0. (Success)
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        """'write_file' function is defined with two optional parameter
        'filename' represents the name of the file to write, while 'text'...
        ...represents the string to be written to the file.
        If no filename or text is provided,it defaults to an empty strings."""
        chars_written = file.write(text)
        return chars_written
        """Finally, the function returns the value of 'chars_written'...
        .....which represents the number of characters written to the file"""
