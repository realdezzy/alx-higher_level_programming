#!/usr/bin/python3
# 2-square.py
"""Define a class Square."""
class Square:
    """A square is a figure with four equal sides and four right angles.

    Args:
    size(int): size of square
    """
    def __init__(self, size=0):
        if type(size).__name__ != 'int':
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
