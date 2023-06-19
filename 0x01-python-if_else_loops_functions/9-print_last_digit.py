#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number < 0:
        number *= -1
    last_digit = 1
    last_numb = number % 10
    if last_digit == 1:
        number *= -1
    print("{:d}".format(last_numb), end="")
    return last_numb
