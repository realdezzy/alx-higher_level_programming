#!/usr/bin/python3

import sys


def infinite_add():
    count = 0
    for x in range(1, len(sys.argv)):
        count = count + int(sys.argv[x])
    print(count)


if __name__ == "__main__":
    infinite_add()
