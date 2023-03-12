#!/usr/bin/python3

""" Import json for serialization and deserialization """
import json


class FileStorage:
    """ Class stores a class object into a file so it can be used """
    __file_path = "file_storage.json"
    __objects = {}

    def all(self):
        """ Return __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """ Sets the key of an object to Classname.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes an object to file """
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(self.__file_path, mode="a+") as f:
            data = json.dumps(new_dict)
            f.write(data)

    def reload(self):
        """ Deserializes an object back into the file storage """
        try:
            with open(self.__file_path) as f:
                string = f.read()
                data = json.loads(string)
                self.__objects = data
        except FileNotFoundError:
            pass
