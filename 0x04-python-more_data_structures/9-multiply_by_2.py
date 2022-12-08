#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
        A function that returns a new dictionary with all values multiplied by 2
    """
    keys = a_dictionary.keys()
    new_dict = {}
    for x in keys:
        new_dict.update({x:a_dictionary.get(x) * 2})
    return new_dict

