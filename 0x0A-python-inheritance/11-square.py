#!/usr/bin/python3
"""This module contains a class named Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This is a child class to the Rectangle class
        Args:
            size(int): The size of the square
        Returns:
            Nothing
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
