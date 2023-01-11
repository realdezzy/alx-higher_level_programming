#!/usr/bin/python3
"""Save Object to file"""
import json


def save_to_json_file(my_obj, filename):
    """Save my_obj to filename in json representation"""

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
