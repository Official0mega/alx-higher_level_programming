#!/usr/bin/python3

"""
File_name: 12-roman_to_int.py
Created: 17th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x04-python-more_data_structures
Status: submitted.
"""


def roman_to_int(roman_string):

    """
    # Technical interview preparation:
    # Create a function that converts a Roman numeral to an integer.
    # You can assume the number will be between 1 to 3999.
    # def roman_to_int(roman_string) must return an integer
    # VARIABLE(" "):
    # roman_to_int(int): Roman to Integer
    # Return: If the roman_string is not a string or None, return 0
    """

    if not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for symbol in reversed(roman_string):
        value = roman_values.get(symbol, 0)

        if value >= prev_value:
            total += value
        else:
            total -= value

        prev_value = value

    return total
