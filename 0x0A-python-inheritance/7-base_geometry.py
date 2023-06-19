#!/usr/bin/python3
"""Updated Implementation of the 'BaseGeometry' class with the 'area' method:
    and the 'integer_validator' methods....
"""

'''
File_Name: 7-base_geometry.py
Created Date: 9th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0A-python-inheritance
Status: Submitted.
'''


class BaseGeometry:
    """
    # Write a class BaseGeometry (based on 6-base_geometry.py)...
    # Public instance method: def area(self): that raises an....
    # Exception with the message area() is not implemented....
    # Public instance method: def integer_validator(self, name...
    # value): that validates value:
    # VARIABLE(" "):
    # Base Geometry(area/integer_validator): Integer validator
    # Return: Always 0. (Success)
    """
    """
    The 'BaseGeometry' class now includes the 'integer_validator' method...
    which validates the given 'value'. It checks if the 'value' is an integer
    and if it is greater than '0'. If any of these conditions are not met..
    the method raises a 'TypeError' or 'ValueError' exception with the
    ...appropriate error message..."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
