#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digits = 0
if number < 0:
    number *= -1
    digits = 1
lst_digit = number % 10
if digits == 1:
    number *= -1
    lst_digit *= -1
print("Last digit of {:d} is ".format(number), end="")
if lst_digit > 5:
    print("{:d} and is greater than 5".format(lst_digit))
elif lst_digit == 0:
    print("{:d} and is 0".format(lst_digit))
else:
    print("{:d} and is less than 6 and not 0".format(lst_digit))
