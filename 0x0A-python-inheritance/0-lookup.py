#!/usr/bin/python3
""" Take object and return its methods"""


def lookup(python_object):
    """ Returns a list of available methods
        and attributes of an object"""
    return dir(python_object)
