#!/usr/bin/python3

""" Import json for the instances to be stored in
JSON format to local storage """

import json


class FileStorage:
    """ Filestorage class converts an instance into a json"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the __objects dictionary """
        return FileStorage.__objects

    def classes_list(self):
        """ locally import BaseModel class"""
        from models.base_model import BaseModel
        info = {
            "BaseModel": BaseModel
        }
        return info

    def new(self, obj):
        """ sets in __objects the object with the key being
        <object classname.id>

        e.g: BaseModel.a6265f3f-6ed3-43cb-9ded-bf90dc4f44a4
        """
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name] = obj

    def save(self):
        """ saves information into JSON file"""
        for key in FileStorage.__objects.keys():
            to_dicts = FileStorage.__objects[key].to_dict()
            FileStorage.__objects[key] = to_dicts
            # FileStorage.__objects.update({key: value.to_dict()})
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as \
                file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """ Deserializes from storage"""
        try:
            with open(FileStorage.__file_path, mode="r", encoding="UTF-8") as\
                    file:
                data = file.read()
                dict_obj = json.loads(data)
            for key, value in dict_obj.items():
                ins = dict_obj[key].get("__class__")
                tmp = self.classes_list()[ins](**value)
                FileStorage.__objects.update({key: tmp})
        except FileNotFoundError:
            pass
