#!/usr/bin/python3
"""Append file"""


def append_write(filename="", text=""):
    """Append and write text to file"""

    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)
    return count
