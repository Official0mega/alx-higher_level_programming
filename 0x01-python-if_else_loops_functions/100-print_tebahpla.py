#!/usr/bin/python3
for teb in reversed(range(ord('a'), ord('z') + 1)):
    if (teb % 2 == 1):
        teb -= 32
    print("{:c}".format(teb), end="")
