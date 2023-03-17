#!/usr/bin/python3

""" Import BaseModel to be used in the instantiation
and saving of instances """

from models.base_model import BaseModel


class State(BaseModel):
    """ Create state class """

    name = ""

    def __init__(self, *args, **kwargs):
        """ init for child class """
        super().__init__(*args, **kwargs)
