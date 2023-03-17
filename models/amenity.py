#!/usr/bin/python3

""" Import BaseModel for class instantiation """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class """

    name = ""

    def __init__(self, *args, **kwargs):
        """ init for amenity """
        super().__init__(*args, **kwargs)
