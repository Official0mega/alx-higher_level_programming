#!/usr/bin/python3
"""
Function that writes an object to a text file using a JSON representation
"""
import json
"""
File_Naime: 5-save_to_json_file.py
Created Date: 13th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0B-python-input_output
Status: Submitted.
"""


def save_to_json_file(my_obj, filename):
    """
    # Write a function that writes an Object to a text file, using a JSON
    # representation:
    # Prototype: def from_json_string(my_str):
    # VARIABLE(" "):
    # from JSON(str): From JSON string to Object
    # Return: Always 0. (Success)
    """
    """
    The 'save_to_json_file' function is defined with two parameters: 'my_obj'
    'which represents the object to be saved, and 'filename', which is the
    name of the file to save the JSON representation of the object..
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
    """
    The 'dump()' functoin takes two arguments: the object to be serialized
    and the file obkject to write the JSON data tp.
    """
