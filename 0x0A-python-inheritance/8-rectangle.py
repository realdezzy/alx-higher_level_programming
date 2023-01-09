#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Base class for Geometric shapes"""

    def area(self):
        """Raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer values

        Args:
            name(str): name param
            value (int): value param

        """

        if (type(value).__name__ != 'int'):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Basic rectangle inheriting from BaseGeometry

    Args:
        width (int): param for width of rectangle
        height (int): param for heiht of the rectangle
    """

    def __init__(self, width, height):

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
