#!/usr/bin/python3
"""Json serializer"""
import json


def to_json_string(my_obj):
    """Returns a serialized version of my_obj"""

    return json.dumps(my_obj)
