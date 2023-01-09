#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Base class for Geometric shapes"""

    def area(self):
        """Raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer values"""

        if (type(value).__name__ != 'int'):
            raise TypeError("<name> must be an integer")
        if (value <= 0):
            raise ValueError("<name> must be greater than 0")
