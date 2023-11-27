#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project"""
import json
import os.path


class Base:
    """The class initializes the base for each instance
    Args:
        id(int): The id for each Base object instantiated
    Attributes:
        __nb_objects(int): A private class attribute to assign an id to a base
                            if not given
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This exchange python hiarachies to JSON string representation
            Args:
            list_dictionaries(dict): The python data structure to
                                    convert to JSON string represenatation
            Returns:
                The JSON string representation
        """
        if not (list_dictionaries or isinstance(list_dictionaries, list)):
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """This exchange JSON string representation to python hiarachies
        Args:
            json_string(str): JSON string represenatation to be converted
                                to python data structure
        Returns:
            The list of the JSON string representation
        """
        if not (json_string or isinstance(json_string, str)):
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """This class method writes the JSON string
            representation of list_objs to a file
        Args:
            list_objs(list): is a list of instances who inherits of Base
                - example: list of Rectangle or list of Square instances
        Retuns:
            A file that contains JSON string representation of the lists_obj
        """
        new_list = list()
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            list_convert = Base.to_json_string(new_list)
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            return file.write(list_convert)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
            Args:
                dictionary(**kwargs): can be thought of as a
                                    double pointer to a dictionary
            Returns:
                an instance with all attributes already set
        """
        if cls.__name__ == "Square":
            tmp = cls(10)
        if cls.__name__ == "Rectangle":
            tmp = cls(10, 12)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
            Args:
                Nothing
            Returns:
                list of instances
        """
        new_list = list()
        if cls.__name__ == "Rectangle":
            path = "./Rectangle.json"
            if not os.path.isfile(path):
                return new_list
        if cls.__name__ == "Square":
            path = "./Square.json"
            if not os.path.isfile(path):
                return new_list
        with open(cls.__name__ + ".json", "r", encoding="utf-8") as file:
            json_string = file.read()
            new_dict_list = cls.from_json_string(json_string)
            for each_dict in new_dict_list:
                obj = cls.create(**each_dict)
                new_list.append(obj)
            return new_list
