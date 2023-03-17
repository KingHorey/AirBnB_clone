#!/usr/bin/python3

""" IMport BaseModel for """
from models.base_model import BaseModel


class User(BaseModel):
    """ Create User class """
    password = ""
    email = ""
    first_name = ""
    last_name = ""

