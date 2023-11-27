#!/usr/bin/python3
"""This module contains a class named Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is a child class to the BaseGeometry class
        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        Returns:
        Nothing
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
