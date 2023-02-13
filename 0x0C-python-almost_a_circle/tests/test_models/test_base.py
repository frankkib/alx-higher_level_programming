#!/usr/bin/python3
"""Test module"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Test cases"""
    def test_id(self):
        b2 = Base(5)
        self.assertEqual(b2.id, 5)

    def test_no_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            b3 = Base(1, 1)

    def test_type(Self):
        with self.assertRaises(TypeError):
            b2 = Base("Invalid Tpype")
