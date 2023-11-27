#!/usr/bin/python3
"""This module contains a function that
    creates an Object from a “JSON file”
"""
from json import loads


def load_from_json_file(filename):
    """This function works as explained above
    Args:
        filename(str): The name of file passed
    Return:
        object file(A Python data structure)
    """
    if type(filename) is not str:
        raise TypeError("the file name must be in string")
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            all_lines = file.read()
            return loads(all_lines)
