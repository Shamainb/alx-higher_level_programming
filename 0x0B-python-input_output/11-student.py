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
        if not (isinstance(first_name, str) and isinstance(last_name, str)
                and isinstance(age, int)):
            raise TypeError("provide the input in the right data type")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dict = dict()
        for string in attrs:
            for k, v in self.__dict__.items():
                if string == k:
                    new_dict[k] = v
        return new_dict

    def reload_from_json(self, json):
        for k, v in json.items():
            if hasattr(self, k):
                if k == "first_name":
                    self.first_name = v
                elif k == "last_name":
                    self.last_name = v
                elif k == "age":
                    self.age = v
