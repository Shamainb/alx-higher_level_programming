#!/usr/bin/python3
"""The module contains a function that prints square using "#"
    The size of the square must be an integer, otherwise riase TypeError
    The size must be greater or equal to zero, otherwise raise ValueError
    """


def print_square(size):
    """The function prints a square
    Args:
        size(int): The size of the square
    Returns:
        Nothing
    """

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be a integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)
    for idx in range(size):
        for j in range(size):
            print('#', end="")
        print()
    print()
