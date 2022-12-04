#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    _max = 0
    for x in my_list:
        if x > _max:
            _max = x
    return _max
