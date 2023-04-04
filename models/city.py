#!/usr/bin/python3

""" import parent class BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ city class for BaseModel """
    state_id = ""
    name = ""
