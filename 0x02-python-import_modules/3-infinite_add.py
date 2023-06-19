#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv_sum = 0
    for arg in sys.argv[1:]:
        argv_sum += int(arg)
    print('{}'.format(argv_sum))
