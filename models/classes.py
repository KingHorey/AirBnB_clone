#!/usr/bin/python3


import json
from uuid import uuid4
import datetime
from BaseModel import *


class State(BaseModel):
    
    def __init__(self, name):
        self.id = uuid4()
        self.name = name
        self.created_at = str(datetime.date.today())
        self.updated_at = str(datetime.date.today())

    @property
    def created_at(self):
        return self.__created_at
    

    def update_info(self, *args, **kwargs):
        x = ["created_at", "updated_at", "id"]
        for i in range(len(args)):
            setattr(self, args[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    

