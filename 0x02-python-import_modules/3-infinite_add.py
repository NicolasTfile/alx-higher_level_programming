#!/usr/bin/python3
from sys import argv
total = 0
for i in argv[1:]:
    total += int(i)
print("{:d}".format(total))
