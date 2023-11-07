#!/usr/bin/python3
"""lookup: return  list of available attributes and methods of an object."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj: Any object

    Returns:
    List of strings representing attributes and methods of the object.
    """
    return dir(obj)
