#!/usr/bin/python3

""" import BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that allows for reviews
    to be made """
    place_id = "" or None
    user_id = "" or None
    text = "" or None

    def __init__(self, *args, **kwargs):
        """ review init"""
        super().__init__(*args, **kwargs)
