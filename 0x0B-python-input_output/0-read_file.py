#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Reads textfile and prints to stdout"""

    with open(filename, encoding="utf-8") as f:
        text = f.read()
    print(text, end="")
