#!/usr/bin/python3
"""This contains test case for the class Square"""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class Test_Square(unittest.TestCase):
    """Contains test case for class Square"""
    def test_init_no_value(self):
        """no value for instantiation"""
        self.assertRaises(TypeError, Square, ())

    def test_isinstance(self):
        """is iinstance of Square"""
        self.assertIsInstance(Square(1), Square)

    def test_sub_class_Rectangle(self):
        """is subclass of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_sub_class_Base(self):
        """is subclass of Base"""
        self.assertTrue(issubclass(Square, Base))

    def test_init_only_size(self):
        """inserting size only"""
        self.assertEqual(Square(10).size, 10)
        self.assertEqual(Square(10).x, 0)
        self.assertEqual(Square(10).y, 0)

    def test_init_all_inputs(self):
        """insering all inputs"""
        s1 = Square(10, 2, 3, 67)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 67)

    def test_value_err_size(self):
        """when size <= 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
            Square(-2)

    def test_type_err_size(self):
        """when size is not integer"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)
            Square("2", 1, 3)

    def test_init_x_no_value(self):
        """instantiate without x value"""
        self.assertEqual(Square(1).x, 0)

    def test_init_x_with_value(self):
        """instantiate with x value"""
        self.assertEqual(Square(2, 5).x, 5)
        self.assertEqual(Square(3, 7, 0).x, 7)
        self.assertEqual(Square(3, 6, 9, 2).x, 6)

    def test_x_type_err(self):
        """x is not integer"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
            Square(2, True, 1, 5)

    def test_x_value_err(self):
        """x < 0"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -2)
            Square(6, -1, 1, 4)

    def test_init_y_no_value(self):
        """instantiate without y value"""
        self.assertEqual(Square(1).y, 0)

    def test_init_y_with_value(self):
        """instantiate with y value"""
        self.assertEqual(Square(2, 5, 5).y, 5)
        self.assertEqual(Square(3, 7, 0).y, 0)
        self.assertEqual(Square(3, 6, 9, 2).y, 9)

    def test_y_type_err(self):
        """y is not integer"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "2")
            Square(2, 1, True, 5)

    def test_y_value_err(self):
        """y < 0"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 2, -2)
            Square(6, 1, -1, 4)

    def test__str__(self):
        """informal output"""
        self.assertEqual(Square(3, 4, 7, 9).__str__(), "[Square] (9) 4/7 - 3")

    def test_update_args(self):
        """positional arguments"""
        s1 = Square(20, 2, 4, 8)
        s1.update(10, 3, 5, 9)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 9)

    def test_upadte_kwargs(self):
        """keyword arguments"""
        s1 = Square(20, 2, 4, 8)
        s1.update(size=15, id=25, y=3, x=17)
        self.assertEqual(s1.size, 15)
        self.assertEqual(s1.id, 25)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.x, 17)

    def test_update_args_kwargs(self):
        """both args and kwargs"""
        s1 = Square(20, 2, 4, 8)
        s1.update(16, 45, size=12, y=6, x=2)
        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.id, 16)
        self.assertEqual(s1.y, 6)
        self.assertEqual(s1.x, 2)

    def test_to_dict(self):
        """converts to dictionary"""
        s1 = Square(10, 2, 1, 9)
        dictionary = {'x': 2, 'y': 1, 'id': 9, 'size': 10}
        self.assertDictEqual(s1.to_dictionary(), dictionary)

    def test_to_dict_type(self):
        """confirm return type"""
        s1 = Square(10, 2, 1, 9).to_dictionary()
        self.assertEqual(type(s1), dict)
