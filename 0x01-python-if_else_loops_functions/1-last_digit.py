#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number)
string1 = f"Last digit of {number} is {num % 10} "
if (num % 10) > 5:
    print(string1 + "and is greater than 5")
elif (num % 10) == 0:
    print(string1 + "and is 0")
elif ((num % 10) < 6) and ((num % 10) != 0):
    print(string1 + "and is less than 6 and not 0")
