#!/usr/bin/python3
"""The module contains a class Rectangle that inherits from Base"""
from .base import Base


class Rectangle(Base):
    """This is a child class to the Base class
    Args:
        Base: The super/parent class
    Attributes:
        __width(int): The width of the rectangle instance which must be > 0
        __height(int): The height of the rectangle instance which must be > 0
        __x(int): Always an integer initialized as 0
        __y(int): Always an integer initialized as 0
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This instantialize an object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Returns the dictionary of an instance of rectangle"""
        new_dict = dict()
        for key, value in self.__dict__.items():
            key = key.replace("_Rectangle__", "")
            new_dict[key] = value
        return new_dict

    def area(self):
        """This returns the area of a the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """This displays the area of a rectangle using '#'"""
        y_row = 0
        while y_row < self.y:
            print()
            y_row += 1
        row = 0
        while row < self.__height:
            column = 0
            x_column = 0
            while x_column < self.__x:
                print(" ", end="")
                x_column += 1
            while column < self.__width:
                print("#", end="")
                column += 1
            print()
            row += 1

    def __str__(self):
        """This returns a user-friendly / informal string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """This updates the fields of an object"""
        artt = ["id", "width", "height", "x", "y"]
        for idx, arg in enumerate(args):
            if idx < len(artt):
                setattr(self, artt[idx], arg)
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    @property
    def width(self):
        """The getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter for x"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
