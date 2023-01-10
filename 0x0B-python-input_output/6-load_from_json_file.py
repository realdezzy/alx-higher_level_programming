#!/usr/bin/python3
"""Load Object from file"""
import json


def load_from_json_file(filename):
    """Load object from filename"""

    with open(filename, encoding="utf-8") as f:
        filex = json.load(f)

    return filex
