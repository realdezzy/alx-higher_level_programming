#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
        Returns a modified list with occurances of
        search changed to the value of replace
    """
    repl = list(map(lambda x: x if x != search else replace, my_list))
    return repl
