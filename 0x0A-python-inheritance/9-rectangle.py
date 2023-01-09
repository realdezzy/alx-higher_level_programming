#!/usr/bin/python3
"""Full Rectangle""" 
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def __str__(self):
        """String representation of rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns the area of the rectangle"""

        return (self.__width * self.__height)

