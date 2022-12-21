#!/usr/bin/python3
# 5-square.py

"""Define a class Square."""

class Square:
    """A square is a figure with four equal sides and four right angles.

    Args:
    size(int): size of square

    Raises:
        TypeError: if a non integer datatype is specified
        ValueError: if value of size is less than 0
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
    @property
    def size(self):
        """Getter property for private instance(size)

        Args:
            value(int): Integer value for size setter

        Returns:
            int:  returns the value of size
        Raise:
            TypeError: if a non integer datatype is specified
            ValueError: if value of size is less than 0
        """
        return self.__size
    @size.setter
    def size(self, value):

        if type(value).__name__ != 'int':
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """ Prints to stdout the square with the character #
        or an empty space if size is 0
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for x in range(self.__size):
                print("{}".format("#"), end="")
            print()
