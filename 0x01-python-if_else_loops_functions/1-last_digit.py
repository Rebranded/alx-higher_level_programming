#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of the number
digit = abs(number) % 10

# Adjust digit for negative numbers
if number < 0:
    digit = -digit

# Use an f-string to print the result
if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
