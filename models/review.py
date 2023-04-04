#!/usr/bin/python3

""" import parent class BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class for AirBnb homes """
    place_id = ""
    user_id = ""
    text = ""
