#!/usr/bin/python3

"""
File_name: 4-hidden_discovery.py
Created: 11th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x02-python-import_modules
Status: submitted.
"""

if __name__ == '__main__':
    from importlib import import_module
    hidden_4 = import_module('hidden_4')
    for name in sorted(dir(hidden_4)):
        if name[0:2] != '__':
            print('{:s}'.format(name))
