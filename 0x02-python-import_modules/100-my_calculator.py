#!/usr/bin/python3

"""
File_name: 100-my_calculator.py
Created: 11th of May, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x02-python-import_modules
Status: submitted.
"""

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) == 4:
        funcs = [('+', add), ('-', sub), ('*', mul), ('/', div)]
        for func in funcs:
            if sys.argv[2] == func[0]:
                a = int(sys.argv[1])
                b = int(sys.argv[3])
                print('{} {} {} = {}'.format(
                    a, func[0], b, func[1](a, b)
                    ))
                sys.exit()
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    else:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)
