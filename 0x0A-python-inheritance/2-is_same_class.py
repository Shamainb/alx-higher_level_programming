#!/usr/bin/python3
"""This module contains a fucntion that checks
    if the object is a type of the class
    """


def is_same_class(obj, a_class):
    """Works as explained in module section
    Args:
        obj: Any object
        class: Any type
    Returns:
        True: if type(obj) is a_class
        False: If otherwise
        """
    if type(obj) is a_class:
        return True
    return False
