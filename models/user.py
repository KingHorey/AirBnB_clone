#!/usr/bin/python3

""" IMport BaseModel for """
from models.base_model import BaseModel


class User(BaseModel):
    """ Create User class """
    password = ""
    email = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ ini class for User"""
        super().__init__(*args, **kwargs)
