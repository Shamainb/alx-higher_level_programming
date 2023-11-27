#!/usr/bin/python3
"""This module contains a class named MyInt
    which inherits the int data type
    """


class MyInt(int):
    """This a child class to int
        Args:
            num(int): The number to print
        Returns:
            as mentioned in each method
        """
    def __init__(self, num):
        self.__num = num

    def __str__(self):
        return "{}".format(self.__num)

    def __eq___(self, value):
        return self.__num != value

    def __ne__(self, value):
        return self.__num == value
