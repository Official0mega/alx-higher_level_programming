#!/usr/bin/fish
"""
This is the shell script written in the Fish shell(another command-line...
.. shell for UNIX-like operating systems). This function is designed to run
unit tests.
"""

'''
File_Name: funcs.fish
Created Date: 19th of June, 2023
Authur: David James Taiye (Official0mega)
Size: Undefined
Project Title: 0x0C-python-almost_a_circle
Status: Submitted.
'''
set PYTHON "python3"
# set PYTHON ~/apps/Python-3.4.10/python

# E.g.; run_u_test base
#   => python3 -m unittest tests/test_models/test_base.py
# E.g.; run_u_test
#   => python3 -m unittest discover tests
function run_u_test
    if test (count $argv) -eq 1
        $PYTHON -m unittest tests/test_models/test_$argv[1].py
    else
        $PYTHON -m unittest discover tests
    end
end
