#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    vals = a_dictionary.values()
    if value not in vals:
        return a_dictionary
    temp = a_dictionary.copy()
    temp_items = temp.items()
    for x in temp_items:
        if x[1] == value:
            a_dictionary.pop(x[0])
