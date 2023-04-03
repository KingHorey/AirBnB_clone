#!/usr/bin/python3

""" import unittesting for testing storage and storage file"""

import unittest
from models.engine import file_storage as f
class TestStorage(unittest.TestCase):
    """ Testing the storage class """
    def test_all(self):
        self.assertTrue(type(dict))

    def test_save(self):
        with self.assertRaises(FileNotFoundError):
            pass

    def test_reload(self):
        with self.assertRaises(FileNotFoundError):
            pass