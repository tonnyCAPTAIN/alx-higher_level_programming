#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    test for max_integer
    """
    def test_max_int_basic(self):
        """
        test for normal list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_int_empty(self):
        """test if list is empmty"""
        self.assertEqual(max_integer([]), None)

    def test_max_int_neg(self):
        """test max negative number"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_int_one(self):
        """tests if list has only one item
        """
        self.assertEqual(max_integer([1]), 1

if __name__ == '__main__':
    unittest.main()
