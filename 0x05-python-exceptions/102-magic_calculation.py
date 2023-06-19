#!/usr/bin/python3

"""
File_name: 102-magic_calculation.py
Created: 29th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x05-python-exceptions
Status: submitted.
"""


def magic_calculation(a, b):

    """
    # that does exactly the same as the following Python bytecode
    # VARIABLE(" "):
    # mafic_calculation(int): ByteCode -> Python #4
    # Returns: Always 0. (Success)
    """
    total_sum = 0
    for x in range(1, 3):
        """The byte code represent a Loop that iterates over range '(1, 4)"""
        try:
            if x > a:
                """Inside this Loop, there is a comparison 'if x > a'"""
                """And if it's true, an exception is raised,
                Otherwise, the calculation below"""
                raise Exception('Too Far')
            total_sum += (a ** b) / x
        except BaseException:
            total_sum = b + a
            break
        """ Finally, the 'total_sum' is returned"""
    return total_sum
