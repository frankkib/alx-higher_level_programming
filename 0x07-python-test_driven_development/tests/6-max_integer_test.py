#!/usr/bin/python3
"""unittest import module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerOfList(unittest.TestCase):
    """Unittest class max"""
    def test_module_docstring(self):
        """tests for module"""
        i = __import__('6-max_integer').__doc__
        self.assertTrue(len(i) > 1)

    def test_function_docstring(self):
        """tests for docstring"""
        num = max_integer.__doC__
        self.assertTrue(len(num) > 1)

    def test_empty_list(self):
        """"test for empty list[]"""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_no_args(self):
        """tets for no arguments"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        element = [1]
        sef.assertEqual(max_integer(element), 1)

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
