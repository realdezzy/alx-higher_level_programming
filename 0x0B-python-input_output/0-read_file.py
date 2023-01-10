#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Reads textfile and prints to stdout"""

    if not filename:
        return
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    print(text)
