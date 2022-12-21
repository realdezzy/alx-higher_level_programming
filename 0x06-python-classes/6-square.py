#!/usr/bin/python3

class Square:
    """A square is a figure with four equal sides and four right angles.

    Args:
    size(int): size of square
    position(tuple): value for position param

    Raises:
        TypeError: if a non integer datatype is specified
        ValueError: if value of size is less than 0
    """
    def __init__(self, size=0, position=(0, 0)):

        if type(size).__name__ != 'int':
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (type(position).__name__ != 'tuple' or
	position[0] < 0 or
	position[1] < 0 or
	len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
    @property
    def position(self):
        """Getter and setter property for private instance(position)

        Setter:
        Args:
            value(tuple):  Tuple value for position setter

        Returns:
            tuple:  returns the value of position
        Raise:
            TypeError: if a non tuple datatype is specified
                        or tuple values are negative integers
        """
        return self.__position

    @position.setter
    def position(self, value):

        if (type(value).__name__ != 'tuple' or
	value[0] < 0 or
	value[1] < 0 or
	len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
