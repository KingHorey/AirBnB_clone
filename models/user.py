#!/usr/bin/python3

""" parent class BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class for creating user instances """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
