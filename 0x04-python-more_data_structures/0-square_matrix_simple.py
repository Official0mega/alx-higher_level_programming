#!/usr/bin/python3

"""
File_name: 0-square_matrix_simple.py
Created: 17th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x04-python-more_data_structures
Status: submitted.
"""


def square_matrix_simple(matrix=[]):

    """
    # Write a function that computes the square value
    # all integers of a matrix.
    # matrix is a 2 dimensional array
    # VARIABLE(" "):
    # Matrix(list): squared simple
    # Returns a new matrix:
    # Same size as matrix
    # Each value should be the square of the value of the input
    """

    # This line creates a new matrix with
    # the same size as the input matrix

    matrix_sequel = [[0 for _ in range(len(row))] for row in matrix]

    #  This line iterate over each element in the matrix

    for repeat in range(len(matrix)):
        for recap in range(len(matrix[repeat])):
            #  This line square the value and assign it to
            #  Corresponding position in the new matrix
            matrix_sequel[repeat][recap] = matrix[repeat][recap] ** 2
    return matrix_sequel


#  simple_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#  squared_matrix = square_matrix_simple(simple_matrix)
#  print(squared_matrix)
#  print(simple_matrix)
