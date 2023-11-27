#!/usr/bin/python3
"""This module contains a function that returns the dictionary
    description with simple data structure (list, dictionary,
    string, integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """Function works as descriped in the module section
        Args:
            obj(object): A Python data structure
        Returns:
            The dictionary of the obj passed
    """
    return obj.__dict__
