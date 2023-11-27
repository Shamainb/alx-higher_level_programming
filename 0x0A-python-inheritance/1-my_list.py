#!/usr/bin/python3
"""This module contains a class that inherits
    the list data structure
    """


class MyList(list):
    """The class is a sub-class of list
        Args:
            list: The list data structure
        Returns:
            Nothing
            """
    def print_sorted(self):
        """A method of MyList class
            that prints a sorted list
        """
        print(sorted(self))
