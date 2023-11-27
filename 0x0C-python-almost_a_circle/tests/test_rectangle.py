#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """The TestCase for class Rectangle"""
    def test_normal_use(self):
        """Test for normal usae"""
        # self.assertEqual(Rectangle(10, 2).id, 3)
        self.assertEqual(Rectangle(10, 2).height, 2)
        self.assertEqual(Rectangle(10, 2).width, 10)
        self.assertEqual(Rectangle(10, 2).x, 0)
        self.assertEqual(Rectangle(10, 2).y, 0)
        self.assertEqual(Rectangle(10, 2, 2, 6).x, 2)
        self.assertEqual(Rectangle(10, 2, 2, 6).y, 6)
        self.assertEqual(Rectangle(10, 2, 2, 6, 42).id, 42)

    def test_instance(self):
        """Test for an instance of Rectangle"""
        self.assertTrue(isinstance(Rectangle(1, 2), Rectangle))
        self.assertIsInstance(Rectangle(1, 2), Rectangle)

    def test_subclass(self):
        """Test for a subclass of Rectangle"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_incomplete_init(self):
        """Test for incomplete data for instantiation"""
        self.assertRaises(TypeError, Rectangle, ())
        self.assertRaises(TypeError, Rectangle, (4))

    def test_value_for_width(self):
        """Test for if width <= 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)
            Rectangle(-1, 1)

    def test_type_for_width(self):
        """Test for if width is not int"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)
            Rectangle("hello", 2)
            Rectangle([1, 2, "3", 3], 1)

    def test_value_for_height(self):
        """Test for if height <= 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
            Rectangle(1, -1)

    def test_type_for_height(self):
        """Test for if height is not int"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)
            Rectangle(2, "hello")
            Rectangle(1, [1, 2, "3", 3])

    def test_x_init_without_value(self):
        """No value for x"""
        self.assertEqual(Rectangle(10, 3).x, 0)

    def test_x_init_with_value(self):
        """Value for x"""
        self.assertEqual(Rectangle(10, 3, 4).x, 4)

    def test_x_value_err(self):
        """x < 0"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 4)

    def test_x_type_err(self):
        """x is not int"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, True)
            Rectangle(10, 2, "2")

    def test_y_init_without_value(self):
        """No value for y"""
        self.assertEqual(Rectangle(10, 3, 5).y, 0)

    def test_y_init_with_value(self):
        """Value for y"""
        self.assertEqual(Rectangle(10, 3, 2, 4).y, 4)

    def test_y_value_err(self):
        """y < 0"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 1, -4)

    def test_y_type_err(self):
        """y is not int"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, True)
            Rectangle(10, 2, 3, "2")

    def test_area(self):
        """Got value for area"""
        self.assertEqual(Rectangle(10, 2).area(), 20)

    def test_str_(self):
        """print a user-friendly or informal output"""
        self.assertEqual(Rectangle(10, 2, 3, 5, 6).__str__(),
                         "[Rectangle] (6) 3/5 - 10/2")

    def test_update_args(self):
        """Upadte with positional arguments"""
        r1 = Rectangle(10, 2)
        r1.update(21, 64, 2, 6, 78)
        self.assertEqual(r1.id, 21)
        self.assertEqual(r1.width, 64)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 78)

    def test_update_kwargs(self):
        """Update with keyword arguments"""
        r1 = Rectangle(10, 2, 5, 7, 8)
        r1.update(height=78, x=15, id=32, y=12)
        self.assertEqual(r1.height, 78)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.x, 15)
        self.assertEqual(r1.y, 12)
        self.assertEqual(r1.id, 32)

    def test_update_args_and_kwargs(self):
        """Update with both *args and **kwargs"""
        r1 = Rectangle(10, 2, 5, 7, 8)
        r1.update(32, 15, 20, width=17, y=3, x=12)
        self.assertEqual(r1.id, 32)
        self.assertEqual(r1.width, 17)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 3)

    def test_to_dict(self):
        """converts to dictionary"""
        r1 = Rectangle(10, 2, 1, 9, 12)
        dictionary = {'x': 1, 'y': 9, 'id': 12, 'height': 2, 'width': 10}
        self.assertDictEqual(r1.to_dictionary(), dictionary)

    def test_to_dict_type(self):
        """confirm return type"""
        r1 = Rectangle(10, 2, 1, 9, 12).to_dictionary()
        self.assertEqual(type(r1), dict)


if __name__ == "__main__":
    unittest.main()
