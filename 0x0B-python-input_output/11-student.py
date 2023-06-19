#!/usr/bin/python3
"""
Updated 'Student' class that includes the 'to_json' method with the ability
..too filter the attributes based on a given list:
"""

'''
File_Naime: 11-student.py
Created Date: 13th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0B-python-input_output
Status: Submitted.
'''


class Student:
    """
    # Write a class Student that defines a student by:(based on 10-student.py)
    # Instantiation with first_name, last_name and age: def
    # __init__(self, first_name, last_name, age):
    # Public method def to_json(self, attrs=None): that retrieves a...
    # dictionary representation of a Student instance
    # (same as 8-class_to_json.py):
    # VARIABLE(" "):
    # Student: Student to disk and reload
    # Return: Always 0. (Success)
    """
    """
    The 'student' class remains the same as same three exercise, with the
    ...same three public instance attributes: 'first_name', 'last_name', and
    ...'age',.. The 'to_json'method is the same as in the previous exercise,
    ..allowing for optional attribute filtering.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if '__dict__' in dir(self):
            res = dict()
            can_filter = False
            if (type(attrs) is list) and all(type(s) is str for s in attrs):
                can_filter = True
            for key in self.__dict__.keys():
                if (not can_filter) or (can_filter and key in attrs):
                    res[key] = self.__dict__[key]
            return res

    def reload_from_json(self, json):
        if isinstance(json, dict) and ('__dict__' in dir(self)):
            # self.__dict__.clear()
            for key in json.keys():
                self.__dict__[key] = json[key]
