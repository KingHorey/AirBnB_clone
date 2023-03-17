#!/usr/bin/python3

""" import BaseModel class for instantiation """

from models.base_model import BaseModel


class City(BaseModel):
    """ Create City class """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
