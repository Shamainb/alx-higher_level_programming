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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            it returns a string representation in human-readble format
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        k = str(self.print_symbol)
        for i in range(self.__height):
            for j in range(self.__width):
                result += k
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
        if Rectangle.number_of_instances == 0:
            return
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 > area2 or area1 == area2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """The classmethod change a rectangle to a square
            width=size=height
        """
        return cls(width=size, height=size)
