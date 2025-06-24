#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([2, 4, 1, 3]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([10]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([-5, 0, 5.5]), 5.5)

    def test_negative(self):
        self.assertEqual(max_integer([-3, -1, -2]), -1)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    def test_non_list(self):
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
