#!/usr/bin/python3

""" import datetime to set created_at, updated_at
and uuid to set id
import storage to save into json file
"""

from datetime import datetime
from uuid import uuid4
from . import storage


class BaseModel:
    """ Base model to be used in instantiation """
    def __init__(self, *args, **kwargs):
        if (kwargs):
            {k: v for k, v in kwargs.items() if k != "__class__"}
            self.created_at = datetime.strptime(kwargs.get('created_at'),
                                                "%Y-%m-%d %H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs.get('updated_at'),
                                                "%Y-%m-%d %H:%M:%S.%f")
            self.id = kwargs.get('id')
            dirs = ["updated_at", "created_at", "id", "__class__"]
            for k, v in kwargs.items():
                if k not in dirs:
                    setattr(self, k, v)
        else:
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            self.id = str(uuid4())
            models.storage.new(self)

    def save(self):
        """ Method updated the updated_at attribute of the object """
        time = datetime.now()
        self.updated_at = time
        #storage.save()

    def to_dict(self):
        """ added __class__ key and value to __dict__
        return value: dictionary """
        self.__dict__.update({"__class__": self.__class__.__name__})
        return ({k: v if isinstance(v, int) else str(v)
                 for k, v in self.__dict__.items()})

    def __str__(self):
        """ returns a printable dict of the instance """
        output = "[" + str(self.__class__.__name__) + "] "
        output += "("+str(self.id)+") " + str(self.__dict__)
        return (output)
