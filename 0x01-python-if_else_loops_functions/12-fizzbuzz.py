#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.

    For multiples of three, then print Fizz instead of the number.
    For multiples of five, then print Buzz instead of the number.
    For multiples of three and five,then  print FizzBuzz instead of the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
