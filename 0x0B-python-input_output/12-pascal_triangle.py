#!/usr/bin/python3
"""A function that generate Pascal's Triangle up to a given number of rows
"""

'''
File_Naime: 12-pascal_triangle.py
Created Date: 13th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0B-python-input_output
Status: Submitted.
'''


def pascal_triangle(n):
    """
    # Technical interview preparation:
    # Create a function def pascal_triangle(n): that returns a list of lists
    # ..of integers representing the Pascal’s triangle of n:
    # VARIABLE(" "):
    # Pascal Triangle(n):  Pascal's Triangle
    # Return: Always 0. (Success)
    """
    """
    The function 'pascal_triangle' takes an integer 'n' as input, which
    represents the number of rows to generate in Pascal's Triangle.
    """
    if n <= 0:
        return []
    trigon = [[] for x in range(n)]
    trigon[0] = [1]
    if n > 1:
        trigon[1] = [1, 1]
    if n > 2:
        for i in range(2, n):
            trigon[i].append(1)
            for j in range(i - 1):
                trigon[i].append(trigon[i - 1][j] + trigon[i - 1][j + 1])
            trigon[i].append(1)
    return trigon
    """Finally, we return the generated 'triangle'"""
