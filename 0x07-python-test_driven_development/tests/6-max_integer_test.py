#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class max"""

    def test_empty_list(self):
        """"test for empty list[]"""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_no_args(self):
        """tets for no arguments"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        element = [1]
        self.assertEqual(max_integer(element), 1)

    def test_positve_end(self):
        """ tests for positive end"""
        end = [2, 56, 54, 78]
        self.assertEqual(max_integer(end), 78)

    def tets_positve_beginning(self):
        """"tests for positive at the beginning"""
        begin = [50, 45, 25, 35]
        self.assertEqual(max_interger(begin), 50)

    def test_positive_middle(self):
        """tests for positive in the middle"""
        middle = [5, 7, 20, 11, 8]
        self.assertEqual(max_integer(middle), 20)

    if __name__ == "__main__":
        unittest.main()
