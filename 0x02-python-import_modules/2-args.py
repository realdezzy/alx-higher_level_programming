#!/usr/bin/python3
from sys import argv



if __name__ == "__main__":
    """Print total number of arguments
    then also print argument number and text
    """
    length = len(argv)
    if length <= 1:
        print("0 arguments.")
        return
    print(f"{length - 1} arguments:") if (length - 1) > 1 \
        else print(f"1 argument:")
    for x in range(1, length):
        print(f"{x}: {argv[x]}")


