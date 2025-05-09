#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
lst_dig = number % 10
if number < 0 and lst_dig != 0:
    last_digit = lst_dig - 10

if last_digit > 5:
    print(f"Last digit of {number} is {lst_dig} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {lst_dig} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {lst_dig} and is less than 6 and not 0")
