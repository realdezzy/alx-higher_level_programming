#!/usr/bin/python3

def uppercase(str):
    """uppercase converts string to uppercase."""
    str_n = str + '\n'
    for i in str_n:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
            print("{}".format(i), end="")
        else:
            print("{}".format(i), end="")
