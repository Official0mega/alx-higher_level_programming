#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
from importlib import import_module


class TestMaxInteger(unittest.TestCase):
    '''
    File_name: 6-max_integer_test.py
    Created: 1st of June, 2023
    Auth: David James Taiye (Official0mega)
    Size: undefined
    Project: 0x07-python-test_driven_development
    Status: submitted.
    '''

    def test_area(self):
        """
        # Since the beginning you have been creating “Interactive tests”....
        # For this exercise, you will add Unittests.
        # All tests you make must be passable by the function below...
        # VARIABLE(" "):
        # Max_integer(List): Max integer - Unittest
        # Return: Always 0. (Success).
        """
        max_integer = import_module('6-max_integer', '..').max_integer
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([7, 2, -3, 45, 6]), 45)
        self.assertEqual(max_integer([7, 2, 45, 6]), 45)
        self.assertEqual(max_integer([-7, -2, -45, -6]), -2)
        self.assertEqual(max_integer([-7, 1, -18, -6]), 1)
        self.assertEqual(max_integer([7, 1, -18, -6]), 7)
        self.assertEqual(max_integer([-7, 1, -18, 9]), 9)
