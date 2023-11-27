#!/usr/bin/python3
"""The module contains a function "matrix_divided"
    The matrix must be a list of lists
    It's elements must be an int or float
    The size of each row must be equal
    """


def matrix_divided(matrix, div):
    """The function wokrs as explained in the module section
    Args:
        matrix(list): This is a list of lists
        div(int or float): This should not be zero(0)
    Returns:
        new_list(list): Contains each element divided by div
    """

    if not isinstance(matrix, list) or not matrix:
        raise TypeError("""matrix must be a matrix (list of lists) of
                integers/floats""")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = list()
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("""matrix must be a matrix (list of lists) of
                    integers/floats""")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_list_row = list()
        for idx in row:
            if type(idx) not in [int, float]:
                raise TypeError("""matrix must be a matrix (list of lists)
                        of integers/floats""")
            new_list_row.append(round(idx / div, 2))
        new_list.append(new_list_row)
    return new_list
