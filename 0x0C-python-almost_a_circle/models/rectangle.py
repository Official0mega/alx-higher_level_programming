#!/usr/bin/python3
"""This is a  part of a module related to working with polygons.
   and it deals with various geometric shapes and polygons.
   The Square class inherits from another class named Rectangle, indicating a
   relationship between squares and rectangles in terms of their properties
   and behaviors.
"""
from .base import Base

'''
File_Name: rectangle.py
Created Date: 18th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0C-python-almost_a_circle
Status: Submitted.
'''


class Rectangle(Base):
    """
    Represents a rectangle polygon with four perpendicular sides and two pairs
    of equal sides.
    Inherits from the base class for polygon objects.

    Attributes:
        width (int):
        The width of the rectangle. height (int): The height of the rectangle.
        x (int): The horizontal position of the rectangle. y (int):
        The vertical
        position of the rectangle. id (int): The unique identifier of the
        rectangle.

        Methods:
        __init__(width, height, x=0, y=0, id=None):
        Initializes a new rectangle object with the specified dimensions and
        position.

        area():
        Computes and returns the area of the rectangle.

        display(): Prints a visual representation of the rectangle using '#'
        characters.

        update(*args, **kwargs):
            Updates the attributes of the rectangle using either non-keyword
            arguments or keyword arguments.

        Args:
            *args (tuple): Non-keyword arguments representing attribute values
            to update.
            **kwargs (dict): Keyword arguments representing
            attribute-value pairs to update.

        to_dictionary():
            Returns a dictionary representation of the rectangle.

        Properties:
            width:
                Gets or sets the width of the rectangle.

            height: Gets or sets the height of the rectangle.
            x:
                Gets or sets the horizontal position of the rectangle.
            y:
                Gets or sets the vertical position of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle object with the specified dimensions
           and position.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The horizontal position of the rectangle.
            Defaults to 0.
            y (int, optional): The vertical position of the rectangle.
            Defaults to 0.
            int, optional): The unique identifier of the rectangle.
            Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets or sets the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Gets or sets the height of the rectangle.
        """
        return self.__height

    @property
    def x(self):
        """
        Gets or sets the horizontal position of the rectangle
        """
        return self.__x

    @property
    def y(self):
        """
        Gets or sets the vertical position of the rectangle.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets the horizontal position of the rectangle.

        Args:
            value (int): The new horizontal position value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets the vertical position of the rectangle.

        Args:
            value (int): The new vertical position value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The computed area.
        """
        return self.width * self.height

    def display(self):
        """
        Prints a visual representation of the rectangle using '#' characters.
        """
        h_off = ' ' * self.x
        h_val = '#' * self.width
        print('\n' * self.y, end='')
        print('{:s}{:s}\n'.format(h_off, h_val) * self.height, end='')

    def __str__(self):
        """Creates a string representation of this polygon.

        Returns:
            str: A string representation of this polygon.
        """
        parts = (
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )
        res = '[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}'.format(
            parts[0], parts[1], parts[2], parts[3], parts[4]
        )
        return res

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle using either non-keyword
        arguments or keyword arguments.

        Args:
            args (tuple): Non-keyword arguments representing attribute
            values to update.
            kwargs (dict): Keyword arguments representing attribute-value
            pairs to update.
        """
        attrs = ('id', 'width', 'height', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
            dict: A dictionary with the attributes of the rectangle.
        """
        res = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return res
