#!/usr/bin/python3
"""This module contains a function that writes
    an Object to a text file, using a JSON representation
"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """This function works as explained above
        Args:
            my_obj(object): A Python data structure
            filename(str): A file name of type str
        Returns:
            Nothing
    """
    if type(filename) is not str:
        raise TypeError("file name must be a string")
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            string = dumps(my_obj)
            file.write(string)
