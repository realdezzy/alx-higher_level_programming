#!/usr/bin/python3
"""Add Item module"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    lst = load_from_json_file("add_item.json")
except FileNotFoundError:
    lst = []
save_to_json_file(lst + sys.argv[1:], "add_item.json")
