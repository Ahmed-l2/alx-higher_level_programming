#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if abs(number) % 10 > 5:
    print(f"Last digit of {number} is {abs(number) % 10} and is greater than 5")
elif abs(number) % 10 == 0:
    print(f"Last digit of {number} is {abs(number) % 10} and is 0")
elif abs(number) % 10 < 6 and abs(number) % 10 != 0:
    print(f"Last digit of {number} is {abs(number) % 10} and is less than 6 and not 0")
