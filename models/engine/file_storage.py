#!/usr/bin/python3

""" Import json for serialization and deserialization """
import json


class FileStorage:
    """ Class stores a class object into a file, so it can be used """
    __file_path = "file_storage.json"
    __objects = {}

    def all(self):
        """ Return self.__objects"""
        return self.__objects

    def new(self, obj):
        """ Sets the key of an object to Classname.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes an object to file """
        # if ()
        new_dict = {}
        for k, v in self.__objects.items():
            if isinstance(v, dict):
                new_dict[k] = v
            else:
                new_dict[k] = v.to_dict()
        with open(self.__file_path, mode="w") as f:
            data = json.dumps(new_dict)
            f.write(data)

    def reload(self):
        """ Deserializes an object back into the file storage """
        try:
            with open(self.__file_path) as f:
                data = json.load(f)
                self.__objects = data
        except FileNotFoundError:
            pass
