#!/usr/bin/python3
def fizzbuzz():
    for space in range(1, 101):
        if space % 15 == 0:
            print("FizzBuzz ", end="")
        elif space % 5 == 0:
            print("Buzz ", end="")
        elif space % 3 == 0:
            print("Fizz ", end="")
        else:
            print("{:d} ".format(space), end="")
