#!/usr/bin/python3

""" import unittesting for testing storage and storage file"""
import os
import unittest
from models.engine.file_storage import FileStorage as f


class TestStorage(unittest.TestCase):
    """ Testing the storage class """
    def setUp(self):
        """ test setup for instantiation"""
        self.storage = f()

    def test_all(self):
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        self.assertTrue(type(self.storage._FileStorage__objects), dict)
        # with self.assertRaises(TypeError):
        #     f.new(self, dict)

    def test_objects(self):
        self.assertTrue(type(self.storage._FileStorage__objects) == dict)

    def test_path(self):
        self.assertTrue(type(self.storage._FileStorage__file_path) == str)

    def test_save(self):
        with open(self.storage._FileStorage__file_path) as fq:
            data = fq.read()
            self.assertIsNotNone(data)

    def test_reload(self):
        self.assertEqual(type(self.storage._FileStorage__objects), dict)



if __name__ == "__main__":
    unittest.main()

