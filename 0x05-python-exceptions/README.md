## 0x05. Python - Exception

## Resources
Read or watch:

Errors and Exceptions
Learn to Program 11 Static & Exception Handling (starting at minute 7)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* Why Python programming is awesome
* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exceptio

## Copyright - Plagiarism
* You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
* You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
* You are not allowed to publish any content of this project.
* Any form of plagiarism is strictly forbidden and will result in removal from the program

# Requirement
## General

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc

## Tasks
## 0. Safe list printing
* mandatory
* Write a function that prints x elements of a list
* Prototype: def safe_print_list(my_list=[], x=0):

## 1. Safe printing of an integers list
* mandatory
* Write a function that prints an integer with "{:d}".format()
* Prototype: def safe_print_integer(value)
:

## 2. Print and count integers
* mandatory
* Write a function that prints the first x elements of a list and only integers
* Prototype: def safe_print_list_integers(my_list=[], x=0):

## 3. Integers division with debug
* mandatory
* Write a function that divides 2 integers and prints the result
* Prototype: def safe_print_division(a, b):

## 4. Divide a list
* mandatory
* Write a function that divides element by element 2 lists
* Prototype: def list_division(my_list_1, my_list_2, list_length):

## 5. Raise exception
* mandatory
* Write a function that raises a type exception.

* Prototype: def raise_exception():
* You are not allowed to import any module

## 6. Raise a message
* mandatory
* Write a function that raises a name exception with a message.

* Prototype: def raise_exception_msg(message="")

## 7. Safe integer print with error message
# Advanced
* Write a function that prints an integer.

* Prototype: def safe_print_integer_err(value):

## 8. Safe function
# Advanced
* Write a function that executes a function safely.

* Prototype: def safe_function(fct, *args):

## 9. ByteCode -> Python #4
# Advanced
* Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

## 10. CPython #2: PyFloatObject
# Advanced
* Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.
* Python lists:
* Prototype: void print_python_list(PyObject *p)
* Python bytes:
Prototype: void print_python_bytes(PyObject *p);
* Python float:
* Prototype: void print_python_float(PyObject *p):

## End

## 
