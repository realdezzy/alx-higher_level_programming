#!/usr/bin/python3
"""Rectangle class that inherits Base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits Base class

    Attributes:
        width (int): width of the rectagle
        height (int): height of the rectangle
        x (int): x axis
        y (int): y axis
        id (int or None): id of the rectangle

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        """Width of the rectangle

        Args:
            w (int): the width

        """
        if type(w) != int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        """Height of the rectangle

        Args:
            h (int): the height

        """
        if type(h) != int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_axis):
        """X axis of the rectangle

        Args:
            x_axis (int): the x axis

        """
        if type(x_axis) != int:
            raise TypeError("x must be an integer")
        if x_axis < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_axis

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y_axis):
        """Y axis of the rectangle

        Args:
            y_axis (int): the y axis

        """
        if type(y_axis) != int:
            raise TypeError("y must be an integer")
        if y_axis < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_axis

    def area(self):
        """Area of rectangle"""

        return self.__width * self.__height

    def display(self):
        """Returns printed rectangle with '#'
        y is newline, x is space
        """

        if self.__y != 0:
            for newline in range(self.__y):
                print()

        for row in range(self.__height):
            print((self.__x * " ") + (self.__width * '#'))

    def __str__(self):
        """Returns formatted information display
        """

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates rectangle values
        """

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Returns dict representation
        """

        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
