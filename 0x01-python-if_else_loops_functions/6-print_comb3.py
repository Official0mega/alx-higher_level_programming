#!/usr/bin/python3
for comb in range(0, 9):
    for extr_comb in range(comb + 1, 10):
        if comb == 8 and extr_comb == 9:
            print("{:d}{:d}".format(comb, extr_comb))
        else:
            print("{:d}{:d}".format(comb, extr_comb), end=", ")
