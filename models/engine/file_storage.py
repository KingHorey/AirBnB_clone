#!/usr/bin/python3

""" Import json for the instances to be stored in
JSON format to local storage """

import json


class FileStorage:
    """ Filestorage class converts an instance into a json"""

    __file_path = "file_storage.json"
    __objects = {}
    def __int__(self):
        self.reload()

    def all(self):
        """ Returns the __objects dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the object with the key being
        <object classname.id>

        e.g: BaseModel.a6265f3f-6ed3-43cb-9ded-bf90dc4f44a4
        """
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        objects_copy = self.__objects.copy()
        new_dict = {}
        for key, value in objects_copy.items():
            if isinstance(value, dict):
                new_dict[key] = value
            else:
                new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserialized the JSON file to the file path """
        try:
            with open(self.__file_path, mode="r") as f:
                data = json.load(f)
                self.__objects = data
        except FileNotFoundError:
            pass

        # new_dict = {}
        # for key, value in data.items():
        #     class_name = data.get("__class__")
        #     if class_name in globals():
        #         tmp_instance = globals()[class_name](**value)
        #         new_dict[key] = tmp_instance
        # self.__objects = new_dict

