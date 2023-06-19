#!/usr/bin/python3
"""Implementation of the 'square' class that inherits from 'Rectangle':
"""

'''
File_Name: 10-square.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


class Square(Rectangle):
    """
    # Write a class Rectangle that inherits from BaseGeometry..
    # ...(task based on 9-rectangle.py)
    # Instantiation with width and height: def __init__(self, width, height):
    # VARIABLE(" "):
    # Square(Rectangle): Square #1
    # width and height must be private. No getter or setter
    # width and height must be positive integers, validated...
    # ....by integer_validator....
    # Return: Always 0. (Success)
    """
    """
    The 'Square' class inherits from 'Rectangle' and has its own constructor.
    The size of the square is passed as an argument to the constructor.
    It is stored in the private attribute '__size' and validated using the..
    'Integer_validator' method.The 'super().__init__(size, size)' line is...
    used to call the constructor of the 'Rectangle' class and pass the size..
    as both the width and height...."""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        The 'area()' method computes the area of the Geometry and returns
        the integer of the Geometry object."""
        return self.__size * self.__size
