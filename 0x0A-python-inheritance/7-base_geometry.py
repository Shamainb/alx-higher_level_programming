#!/usr/bin/python3
"""This module contains an a class named
    BaseGeometry.
    """


class BaseGeometry:
    """This contains one method"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
