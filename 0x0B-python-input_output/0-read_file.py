#!/usr/bin/python3
"""Function that reads a text file and prints its contents to stdout:
"""

'''
File_Naime: 0-read_file.py
Created Date: 13th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0B-python-input_output
Status: Submitted.
'''


def read_file(filename=""):
    """
    # Write a function that reads a text file (UTF8) and prints it to stdout:
    # Prototype: def read_file(filename=""):
    # You must use the with statement
    # VARIABLE(" "):
    # Read File(filename): 0. Read file
    # Return: Always 0. (Success)
    """
    with open(filename, encoding='utf-8') as file:
        """'read_file' function is defined with an optional parameter
        'filename' that represents the name of the text file to be read. if...
        no file name is provided, it defaults to an empty string."""
        file_contents = file.read()
        print(file_contents, end="")
        """Finally, 'print(file_contents, end="")' is used to print the...
        .....content to stdout. The 'end=""' argument ensures there's no....
        ...extra newline character added at the end of the printed content."""
