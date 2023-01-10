#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """Writes text to file"""

    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
