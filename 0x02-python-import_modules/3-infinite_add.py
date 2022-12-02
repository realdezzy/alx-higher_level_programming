#!/usr/bin/python3

from sys import argv


if __name__ == "__main__":
    count = 0
    for x in range(1, len(argv)):
        count = count + int(argv[x])
    print(count)
