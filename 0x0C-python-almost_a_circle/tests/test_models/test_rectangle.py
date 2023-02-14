#!/usr/bin/python3
"""test modules"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test cases"""
    def test_no_args(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_many_args(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 2, 2, 2, 2, 2, 2)
