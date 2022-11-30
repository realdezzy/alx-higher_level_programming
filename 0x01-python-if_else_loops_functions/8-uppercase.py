#!/usr/bin/python3

def uppercase(str):
    holder = ""
    for x in str:
        if ord(x) >= 97 and ord(x) < 123:
            holder = holder + chr(ord(x) - 32)
        else:
            holder = holder + x
    print(holder)
    return
