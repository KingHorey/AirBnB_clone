#!/usr/bin/python3

import datetime
from uuid import uuid4
import json


class BaseModel:
    """ Base model to be used in instantiation """
    def __init__(self, *args, **kwargs):
        if (kwargs):
            {k: v for k, v in kwargs.items() if k != "__class__"}
            self.created_at = datetime.datetime.strptime(kwargs.get('created_at'), "%Y-%m-%d %H:%M:%S.%f")
            self.updated_at = datetime.datetime.strptime(kwargs.get('updated_at'), "%Y-%m-%d %H:%M:%S.%f")
            self.id = kwargs.get('id')
        else:
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            self.id = str(uuid4())

    def save(self):
        """ Method updated the updated_at attribute of the object """
        time = datetime.datetime.now()
        self.updated_at = time

    def to_dict(self):
        """ added __class__ key and value to __dict__"""
        self.__dict__.update({"__class__": self.__class__.__name__})
        return ({k: v if isinstance(v, int) else str(v)
                 for k, v in self.__dict__.items()})

    def __str__(self):
        """ returns a printable dict of the instance """
        output = "[" + str(self.__class__.__name__) + "] "
        output += "("+str(self.id)+") " + str(self.__dict__)
        output.strip()
        return (output)
