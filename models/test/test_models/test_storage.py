#!/usr/bin/python3

""" import unittesting for testing storage and storage file"""

import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from models.engine.file_storage import FileStorage as f
from models.base_model import BaseModel


class TestStorage(unittest.TestCase):
    """ Testing the storage class """
    def test_all(self):
        self.assertEqual(type(f.all(self)), dict)

    def test_new(self):
        dict_test = {"created_at": "2023-04-03T02:04:42.855400",
                     "updated_at": "2023-04-03T02:04:42.855458",
                     "id": "bd893fc8-5d39-4d91-bda2-7963c5c8ce85",
                     "name":"My_First_Model", "my_number": 89, "__class__":
                         BaseModel}
        r = BaseModel(**dict_test)
        self.assertTrue(type(f._FileStorage__objects), dict)

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
