#!/usr/bin/python3


""" The datetime module is used to know the time and date the
instance was created and the uuid module for getting the unique
identifier of each instance """

import datetime
import uuid


class BaseModel:
    """ BaseModel class contains the common attributes
    that each child class would share from

    Basic Attributes are:
    1. created_at: The date and time that the instance was created
    2. updated_at: The date and time that the instance after being created
    was updated with new information. By default, shares created_at value when
    an instance is created
    3. id: The unique identifier for each instance
    Note: id has been converted to a string """

    def __init__(self, *args, **kwargs):
        """class initialsation method"""
        if (**kwargs):
            self.created_at = datetime.datetime.strptime(
                            kwargs.get("created_at"), "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.datetime.strptime(
                            kwargs.get("updated_at"), "%Y-%m-%dT%H:%M:%S.%f")
            self.id = kwargs.get("id")
            dirs = ["created_at", "updated_at", "id", "__class__"]
            for k, v in kwargs.items():
                if k not in dirs:
                    setattr(self, k, v)
        else:
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())

    def __str__(self):
        """ returns a printable information of instance """
        result = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
        return result

    def save(self):
        """ updates the attribute update_at"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Method returns a dictionary representation of the instance ""
        and adds the class name to the dictionary """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return (new_dict)
