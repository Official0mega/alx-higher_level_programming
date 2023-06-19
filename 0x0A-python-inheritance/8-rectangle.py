#!/usr/bin/python3
"""Implementation of the 'rectangle' class that inherits from 'BaseGeometry'
"""

'''
File_Name: 8-rectangle.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


class Rectangle(BaseGeometry):
    """
    # Write a class Rectangle that inherits from BaseGeometry..
    # ....(7-base_geometry.py).
    # Instantiation with width and height: def __init__(self, width, height):
    # VARIABLE(" "):
    # Rectangle(BaseGeometry): Rectangle
    # width and height must be private. No getter or setter
    # width and height must be positive integers, validated...
    # ....by integer_validator....
    # Return: Always 0. (Success)
    """
    """
    The 'Rectangle' class has a constructor '__init__' that takes 'width' and
    ...'height' as parameters. The width and height are set as private...
    attributes('_-width' and 'height')within the class. The 'integer_
    ..validator' method from the 'BaseGeometry' class is called to validate
    ..the width and height, ensuring they are positive integers"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
