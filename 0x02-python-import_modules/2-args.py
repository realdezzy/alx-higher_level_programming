#!/usr/bin/python3
import sys


def print_args():
    length = len(sys.argv)
    if length <= 1:
        print("0 arguments.")
        return
    print(f"{length - 1} arguments:") if (length - 1) > 1 \
        else print(f"1 argument:")
    for x in range(1, length):
        print(f"{x}: {sys.argv[x]}")


if __name__ == "__main__":
    print_args()
