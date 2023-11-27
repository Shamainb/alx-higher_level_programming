#!/usr/bin/python3
"""This module defines a class named Student"""


class Student:
    """The class instantiates an object with
        first_name, last_name age.
        Attributes:
            first_name(str): First_name
            last_name(str): Last_name
            age(int): Age
        Returns:
            dictionary representation of an instance
    """
    def __init__(self, first_name, last_name, age):
        if type(first_name) is not str and type(last_name) is not str \
                and type(age) is not int:
            raise TypeError("provide the input in the right data type")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
