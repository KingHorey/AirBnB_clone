#!/usr/bin/python3

""" Import json for the instances to be stored in
JSON format to local storage """

import json


class FileStorage:
    """ Filestorage class converts an instance into a json"""

    __file_path = "file_storage.json"
    __objects = {}

    def all(self):
        """ Returns the __objects dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the object with the key being
        <object classname.id>

        e.g: BaseModel.a6265f3f-6ed3-43cb-9ded-bf90dc4f44a4
        """
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[name] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        # self.reload()
        save_dict = {}
        new_dict = FileStorage.__objects.copy()
        for key, value in new_dict.items():
            save_dict.update({key: value.to_dict()})
        with open(FileStorage.__file_path, mode="w") as f:
            json.dump(save_dict, f)

    def reload(self):
        """ deserialized the JSON file to the file path """
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                data = f.read()
            content = json.loads(data)
            for key, data in content.items():
                keys = data.get('__class__')
                if keys in globals():
                    tmp_instance = globals()[keys](**data)
                    FileStorage.__objects = tmp_instance
        except FileNotFoundError:
            pass
