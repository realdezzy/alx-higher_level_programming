#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
        A function that deletes a key in a dictionary.
    """
    try:
       a_dictionary.pop(key)
    except:
        #Shhh
        #Throws key error if pop fails
        pass
    return a_dictionary
