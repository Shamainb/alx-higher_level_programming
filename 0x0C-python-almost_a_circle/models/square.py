#!/usr/bin/python3
"""The module contains a class Square that inherits from Rectangle and Base"""
from .rectangle import Rectangle


class Square(Rectangle):
    """This is a child class to Rectangle
    Attrs:
        size(int): The size of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def to_dictionary(self):
        """Returns dictionary for Square instance"""
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key == "_Rectangle__height":
                continue
            key = key.replace("_Square__", "")
            key = key.replace("_Rectangle__", "")
            if key == "width":
                key = "size"
            new_dict[key] = value
        return new_dict

    @property
    def size(self):
        """The getter for attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of Square with unlimited
            number of positional arguments and keyword
            arguments
            Args:
                args: positional arguments
                kwargs: keyword arguments
        """
        attributes = ["id", "size", "x", "y"]
        for idx, arg in enumerate(args):
            if idx < len(attributes):
                setattr(self, attributes[idx], arg)
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
