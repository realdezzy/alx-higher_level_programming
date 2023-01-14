#!/usr/bin/python3
"""RectangleModule"""

from models.base import Base


class Rectangle(Base):
    """ Representation of a rectangle

        Args:
            width (int): width of rect
            height (int): Height of rect
            x (int): x param
            y (int): y param
            id (int): instance id

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.

    """

    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

            Args:

            value (int): new width value

            Raises:

                TypeError: throws when value is not int

        """

        if (type(value) is not int):
            raise TypeError("Only integers can be set")

        self.__width = value

    @property
    def height(self):
        """Getter for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

            Args:

            value (int): new value

            Raises:

                TypeError: throws when value is not int

        """

        if (type(value) is not int):
            raise TypeError("Only integers can be set")

        self.__height = value

    @property
    def x(self):
        """Getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x

            Args:

            value (int): new value

            Raises:

                TypeError: throws when value is not int

        """

        if (type(value) is not int):
            raise TypeError("Only integers can be set")

        self.__x = value


    @property
    def y(self):
        """Getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y

            Args:

            value (int): new value

            Raises:

                TypeError: throws when value is not int

        """

        if (type(value) is not int):
            raise TypeError("Only integers can be set")

        self.__y = value
