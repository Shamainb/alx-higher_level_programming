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

    def area(self):
        """The method returns the area of the Reactangle
            it's a Public method
        """
        return self.__width * self.__height

    def perimeter(self):
        """This method returns the perimeter of the rectangle
            if width or height is 0, the perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """The method returns/prints an informal or user-friendly
            values of the rectangle using '#' character
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += '#'
            if i == self.__height - 1:
                break
            result += '\n'
        return result

    def __repr__(self):
        """The method returns a formal value of the rectangle
       Returns:
            returns a printable representation of the object in a format that
            can be used to recreate the object
           """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """The method deletes an instance of class Rectangle"""
        print("Bye rectangle...")
