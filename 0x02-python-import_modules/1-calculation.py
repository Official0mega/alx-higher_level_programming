#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    funcs = [('+', add), ('-', sub), ('*', mul), ('/', div)]
    for func in funcs:
        print('{} {} {} = {}'.format(a, func[0], b, func[1](a, b)))
