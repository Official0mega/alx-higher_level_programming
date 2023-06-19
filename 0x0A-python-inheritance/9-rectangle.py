#!/usr/bin/python3
"""Updated Implementation of the 'rectangle' class that inherits from 'BaseGeometry'
"""

'''
File_Name: 9-rectangle.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


class Rectangle(BaseGeometry):
    """
    # Write a class Rectangle that inherits from BaseGeometry..
    # ....(7-base_geometry.py).(task based on 8-rectangle.py)
    # Instantiation with width and height: def __init__(self, width, height):
    # VARIABLE(" "):
    # Rectangle(BaseGeometry): Full rectangle
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

    def area(self):
        """
        The 'area()' method is implemented to calculate the area of the....
        rectangle by multiplying its width and height."""
        return self.__width * self.__height

    def __str__(self):
        """
        The '__str__' method is overridden to return a string representation
        of the rectangle in the desired format...."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
