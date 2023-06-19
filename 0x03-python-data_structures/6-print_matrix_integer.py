#!/usr/bin/python3

"""
File_name: 6-print_matrix_integer.py
Created: 13th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def print_matrix_integer(matrix=[[]]):

    """
    # Write a function that prints a matrix of integers.
    # VARIABLE(" "):
    # print_matrix_integer(list) Lists of lists = Matrix
    # You are not allowed to cast integers into strings
    # You have to use str.format() to print integers
    """
    for row in matrix:
        for i in range(len(row)):
            print('{:d}'.format(row[i]), end=(' ' * (i < len(row) - 1)))
        print('')
