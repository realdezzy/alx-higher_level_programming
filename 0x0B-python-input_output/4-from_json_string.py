#!/usr/bin/python3
"""Json deserializer"""
import json


def to_json_string(my_str):
    """Returns a deserialized version of my_str"""

    return json.load(my_str)
