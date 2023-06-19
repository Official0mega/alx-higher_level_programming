#!/usr/bin/python3
def uppercase(str):
    for case in str:
        if ord(case) >= ord('a') and ord(case) < ord('z') + 1:
            case = chr(ord(case) - 32)
        print('{:s}'.format(case), end="")
    print()
