#!/usr/bin/python3
"""Test module"""
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):
    """Test cases"""
    def test_id(self):
        b2 = Base(5)
        self.assertEqual(b2.id, 5)

    def test_no_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_no_json(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_empty(self):
        self.assertEqual(Base.from_json_string(""), [])
