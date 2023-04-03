#!/usr/bin/python3

""" import statement for other files """

import unittest
from models.base_model import BaseModel as base
import datetime


class TestBaseModel(unittest.TestCase):
    """ Test cases for BaseModel """
    def setUp(self) -> None:
        self.b = base()

    def test_args_init(self):
        """ test init """
        self.assertEqual(type(base()), base)

    def test_print(self):
        self.assertEqual(type(self.b.__str__()), str)

    def test_to_dict(self):
        """ test to_dict method """
        self.assertTrue(type(self.b.to_dict() == dict))

    def test_save(self):
        """ test base_model save's method """
        self.assertEqual(type(self.b.updated_at), datetime.datetime)

