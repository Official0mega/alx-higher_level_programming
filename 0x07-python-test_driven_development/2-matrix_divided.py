#!/usr/bin/python3
""" matrix_divided function
"""

'''
File_name: 2-matrix_divided.py
Created: 3rd of June, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x07-python-test_driven_development
Status: submitted.
'''


def matrix_divided(matrix, div):
    """
    # Write a function that divides all elements of a matrix.
    # All elements of the matrix should be divided by div...
    # ...rounded to 2 decimal places
    # VARIABLE(" "):
    # Matrix_Divided(List): Divide a matrix
    # Return: a new matrix

    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): The matrix to be divided. Must be a matrix
        ...(list of lists)....
        ...containing integers or floats....
        div (int or float): The divisor.

    Returns:
        list: A new matrix with each element divided by the given divisor,
        ....ounded to 2 decimal places...

    Raises:
        TypeError: If the matrix is not a valid matrix (list of lists) of
        integers/floats, or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.

        ## For instance
        matrix = [[1, 2, 3], [4, 5, 6]]
        div = 2
        result = matrix_divided(matrix, div)
        # Output: [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """

    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    size_check = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of '
                    'integers/floats')
        if size_check == 0:
            size_check = len(row)
        elif size_check != len(row):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(num / div, 2) for num in row] for row in matrix]
