#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
        Return a list of all matrix values squared
    """
    sqrd = list(map(lambda x: [i**2 for i in x],matrix))
    return sqrd
