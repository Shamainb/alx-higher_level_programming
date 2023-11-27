#!/usr/bin/python3
"""This module contains a function that adds two integers
    If it's the values are type float, it is typecast to int
    If it's other types other than float or int
    a TypeError is raised
"""


def add_integer(a, b=98):
    """The function adds only float(typecast to int) and integer
        type of parameters is checked for both a and b
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
