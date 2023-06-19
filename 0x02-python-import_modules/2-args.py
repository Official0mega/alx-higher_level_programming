#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    i = 1
    argc = len(sys.argv) - i
    print('{} argument{}{}'.format(
        argc, 's' * (argc != 1),
        ':' if argc > 0 else '.'
        ))
    for arg in sys.argv[i:]:
        print('{}: {}'.format(i, arg))
        i += 1
