#!/usr/bin/python3

def only_diff_elements(set_1: set, set_2: set):
    """
        Returns the symmetric difference between the sets
    """
    new_set = set_1.symmetric_difference(set_2)
    return new_set
