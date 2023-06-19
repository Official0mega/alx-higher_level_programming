#!/usr/bin/python3
""" Numpy Module
"""
import numpy

'''
File_name: 101-lazy_matrix_mul.py
Created: 1st of June, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x07-python-test_driven_development
Status: submitted.
'''


def lazy_matrix_mul(m_a, m_b):
    """
    # Write a function that multiplies 2 matrices by using the module NumPy...
    # Test cases should be the same as 100-matrix_mul but with....
    # new exception type/message
    # VARIABLE(" "):
    # Lazy_Numpy: Lazy matrix multiplication
    # Return: Always 0. (Success).
    """
    return numpy.matmul(m_a, m_b)
