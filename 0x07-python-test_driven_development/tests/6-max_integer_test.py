#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A sub-class of the unittest.TestCase class
    """

    def test_list(self):
        """Tests for non-error generating values"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer(['a', 'b', 'd', 'c']), 'd')
        self.assertEqual(max_integer(["abc", "aaa"]), "abc")
        self.assertEqual(max_integer(["hello", "world", "peace"]), "world")
        self.assertEqual(max_integer(["1", "4", "3", "2"]), "4")
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(["Hello", "WOrld", "wOrld"]), "wOrld")

    def test_type_errror(self):
        """Test for error generating values"""
        self.assertRaises(TypeError, max_integer, ['a', 1, 'd', 'c'])
        self.assertRaises(TypeError, max_integer, [True, None])
        self.assertRaises(TypeError, max_integer, [2 + 5j, 2 - 5j])
        self.assertRaises(TypeError, max_integer, ['a', 1, 'd', 'c'])


if __name__ == "__main__":
    unittest.main()
