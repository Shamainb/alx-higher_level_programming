#!/usr/bin/python3
"""This module contains a class named Rectangle
    which defines the height and width of rectangle
    """


class Rectangle:
    """The class Rectangle
    Args:
        width(int): This is an integer that represents the rectangle width
        height(int): An integer that represents the rectangle height
    Attributes:
        self.width: An object attribute for the width
        self.height: An object attribute for the height
    Returns:
        Nothing
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter for the attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter for the attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter for the attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter for the attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
