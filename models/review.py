#!/usr/bin/python3

""" import BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that allows for reviews
    to be made """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
