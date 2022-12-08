#!/usr/bin/python3

def best_score(a_dictionary):
    """
        Returns a key with the biggest integer value.
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    vals = a_dictionary.values()
    _max = max(vals)
    key = ""
    for k in a_dictionary.items():
        for v in k:
            if v == _max:
                key = k[0]
    return key
