#!/usr/bin/python3
"""This module contains a function that returns
    an object (Python data structure) represented
    by a JSON string
"""
from json import loads


def from_json_string(my_str):
    """This function works as explained in the
        module section.
        Args:
            my_str(str): A string to be exchanged to
                        Python data structure
        Returns:
            The Python data structure
    """
    return loads(my_str)
