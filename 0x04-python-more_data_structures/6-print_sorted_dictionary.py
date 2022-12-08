#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
        A function that prints a dictionary by ordered keys.
    """
    if a_dictionary is None:
        return
    sort_keys = sorted(a_dictionary.keys())
    for x in sort_keys:
        print("{}: {}".format(x, a_dictionary.get(x)))
