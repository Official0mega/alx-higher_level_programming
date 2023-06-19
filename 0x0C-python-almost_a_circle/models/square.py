#!/usr/bin/python3
"""The 'square' class is defined within a module(Rectangle) and it contains
   classes for working with Polygons
"""
from .rectangle import Rectangle

'''
File_Name: square.py
Created Date: 19th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0C-python-almost_a_circle
Status: Submitted.
'''


class Square(Rectangle):
    """
    Represents a square polygon with four equal sides and four right angles.
    The Square class is a subclass of the Rectangle class, inheriting its
    properties and methods. It adds specific functionality and behavior
    for working with squares.

    Attributes:
            size (int): The length of each side of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object.

        Args:
            size (int): The length of each side of the square.
            x (int, optional): The x-coordinate of the square's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
            Defaults to 0.
            id (int, optional): The unique identifier of the square.
            Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets or sets the size (length of each side) of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size (length of each side) of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        parts = (
            self.id,
            self.x,
            self.y,
            self.width
        )
        sqr = '[Square] ({}) {:d}/{:d} - {:d}'.format(
            parts[0], parts[1], parts[2], parts[3]
        )
        return sqr

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            args (tuple): Variable-length arguments representing non-keyword
            arguments.
            kwargs (dict): Arbitrary keyword arguments representing
            attribute-value pairs.
        """
        attrs = ('id', 'size', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """
        Creates a dictionary representation of the square.

        Returns:
            dict: A dictionary representation of the square.
        """
        sqr = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return sqr
