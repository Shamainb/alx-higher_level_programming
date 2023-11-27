#!/usr/bin/python3
"""This module contains a function
    that returns a list of lists of
    integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """The function returns a Pascal trinagle
        Args:
            n(int): The height of triangle
        Returns:
            A Pascal triangle of height n
    """
    if not isinstance(n, int):
        raise TypeError("inside an integer for the height of triangle")
    matrix = list()
    total_column = 1
    row = 0
    while row < n:
        matrix_row = list()
        j = 0
        k = 1
        column = 0
        while column < total_column:
            if column == 0:
                matrix_row.append(1)
            elif column == total_column - 1:
                matrix_row.append(1)
            else:
                matrix_row.append(matrix[row - 1][j] + matrix[row - 1][k])
                j += 1
                k += 1
            column += 1
        total_column += 1
        matrix.append(matrix_row)
        row += 1
    return matrix
