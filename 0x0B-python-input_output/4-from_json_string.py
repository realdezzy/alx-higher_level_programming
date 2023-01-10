#!/usr/bin/python3
"""Json deserializer"""
import json


def from_json_string(my_str):
    """Returns a deserialized version of my_str"""

    return json.loads(my_str)
