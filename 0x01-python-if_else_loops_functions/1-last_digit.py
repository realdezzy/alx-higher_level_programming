#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = -1 * ((-1 * number) % 10) if (number < 0) else number % 10
init_string = f"Last digit of {number} is {last_digit} and "

if last_digit == 0:
    print(init_string + "is 0")
elif last_digit < 6:
    print(init_string + "is less than 6 and not 0")
elif last_digit > 5:
    print(init_string + "is greater than 5")
