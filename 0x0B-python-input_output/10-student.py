#!/usr/bin/python3
"""
Updated 'Student' class that defines a student and includes a 'to_json'
method to retrieve a dictionary representation of a 'Student' instance
"""

'''
File_Naime: 10-student.py
Created Date: 13th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0B-python-input_output
Status: Submitted.
'''


class Student:
    """
    # Write a class Student that defines a student by:
    # VARIABLE(" "):
    # To JSON(self): Student to JSON
    # Return: Always 0. (Success)
    """
    """
    The 'student' class has three public instance attributes:
    'first_name', last_name', and 'age'. These attributes instantiation of a
    'Student' object using the '__init__' method
    """
    """
    The 'to_json' method returns a dictionary representation of the 'Student'
    instance. it creates a dictionary with keys '"first_name"', '"last_name"',
    amd '"age"', and sets their corresponding values to the 'first_name',
    'last_name', and 'age' attributes of the 'Student' instance, respectively.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This returns a dictionary representation of the Student instance
        with optional filtering
        """
        if '__dict__' in dir(self):
            attr = dict()
            filtered_dict = False
            if (type(attrs) is list) and all(type(s) is str for s in attrs):
                filtered_dict = True
            for key in self.__dict__.keys():
                if (not filtered_dict) or (filtered_dict and key in attrs):
                    attr[key] = self.__dict__[key]
            return attr
