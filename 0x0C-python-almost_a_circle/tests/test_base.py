#!/usr/bin/python3
"""Tests for the base.py module"""
import unittest
from models.base import Base
import json
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """The testcase for the Test_Base"""
    def test_id_without_init(self):
        """initiated without given value for id"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_id_with_init(self):
        """Initiated with value for id"""
        self.assertEqual(Base(30).id, 30)

    def test_to_json_str_no_dict(self):
        """input no a list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_str_dict(self):
        """input a list of dictionaries"""
        r1 = Rectangle(10, 7, 2, 8, 6)
        to_dict1 = r1.to_dictionary()
        string = '[{"x": 2, "width": 10, "id": 6, "height": 7, "y": 8}]'
        self.assertCountEqual(Base.to_json_string([to_dict1]), string)

    def test_to_json_str_dict_type(self):
        """input a list of dictionaries"""
        r1 = Rectangle(10, 7, 2, 8, 6)
        to_dict1 = r1.to_dictionary()
        self.assertEqual(type(Base.to_json_string([to_dict1])), str)


if __name__ == "__main__":
    unittest.main()
