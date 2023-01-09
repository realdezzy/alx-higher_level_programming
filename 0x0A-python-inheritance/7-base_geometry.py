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
