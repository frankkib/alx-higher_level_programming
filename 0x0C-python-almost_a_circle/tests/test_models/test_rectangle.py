#!/usr/bin/python3
"""test modules"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test cases"""
    def test_no_args(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_rectangle_has_id(Self):
        r3 = Rectangle(3, 5)
        self.assertEqual(r3.id, 2)

    def test_many_args(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 2, 2, 2, 2, 2, 2)
