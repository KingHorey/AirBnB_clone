#!/usr/bin/python3

""" import unittesting for testing storage and storage file"""
import os
import unittest
from models.engine.file_storage import FileStorage as f


class TestStorage(unittest.TestCase):
    """ Testing the storage class """

    def test_all(self):
        self.assertEqual(type(f.all(self)), dict)

    def test_new(self):
        self.assertTrue(type(f._FileStorage__objects), dict)
        # with self.assertRaises(TypeError):
        #     f.new(self, dict)

    def test_objects(self):
        self.assertTrue(type(f._FileStorage__objects), dict)

    def test_path(self):
        with self.assertRaises(FileNotFoundError):
            with open(f._FileStorage__file_path) as file:
                f.read()

    def test_save(self):
        with self.assertRaises(FileNotFoundError):
            with open("te.txt") as fq:
                f.save(self)

    def test_reload(self):
        with self.assertRaises(FileNotFoundError):
            with open("te.txt") as fq:
                f.reload(self)




if __name__ == "__main__":
    unittest.main()

