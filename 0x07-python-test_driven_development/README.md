## 0x07. Python - Test-driven development

## Important notice on intranet checks for Python projects
## Starting from today:

* Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
* The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case. But not in the implementation of them!
* Don’t trust the user, always think about all possible edge cases

## Learning Objectives
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* Why Python programming is awesome
* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases


## 0. Integers addition
mandatory
Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):
* File: 0-add_integer.py, tests/0-add_integer.txt



## 1. Divide a matrix
mandatory
Write a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
* File: 2-matrix_divided.py, tests/2-matrix_divided.txt



## 2. Say my name
mandatory
Write a function that prints My name is <first name> <last name>

Prototype: def say_my_name(first_name, last_name=""):
* File: 3-say_my_name.py, tests/3-say_my_name.txt 




## 3. Print square
mandatory
Write a function that prints a square with the character #.

Prototype: def print_square(size):
* 4-print_square.py, tests/4-print_square.txt




## 4. Text indentation
mandatory
Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
Prototype: def text_indentation(text):
* File: 5-text_indentation.py, tests/5-text_indentation.txt



## 5. Max integer - Unittest
mandatory
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function def max_integer(list=[]):.
* File: tests/6-max_integer_test.py 


## 6. Matrix multiplication
#advanced
Write a function that multiplies 2 matrices:

Read: Matrix multiplication - only Matrix product (two matrices)

Prototype: def matrix_mul(m_a, m_b):
* File: 100-matrix_mul.py, tests/100-matrix_mul.txt



## 7. Lazy matrix multiplication
#advanced
Write a function that multiplies 2 matrices by using the module NumPy

To install it: pip3 install numpy==1.15.0

Prototype: def lazy_matrix_mul(m_a, m_b):
* File: 101-lazy_matrix_mul.py, tests/101-lazy_matrix_mul.txt



## 8. CPython #3: Python Strings
#advanced

Create a function that prints Python strings.

Prototype: void print_python_string(PyObject *p);
* File: 102-python.c


#End
