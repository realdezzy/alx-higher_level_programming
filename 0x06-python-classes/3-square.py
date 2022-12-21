#!/usr/bin/python3
# 3-square.py
"""Define a class Square."""


class Square:
    """A square is a figure with four equal sides and four right angles.

    Args:
    size(int): size of square

    Raises:
        TypeError: if a non integer datatype is specified
        ValueError: if vslue of size is less than 0
    """
    def __init__(self, size=0):

        if type(size).__name__ != 'int':
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area

        Args:

        Returns:
            int:  returns the current square area
        """
        return (self.__size ** 2)
