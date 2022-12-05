#!/usr/bin/python3
for x in range(0, 100):
    print("{:d}, ".format(x), end="") if (x <= 99) else print("{x}".format(x))
