#!/usr/bin/python3

""" Import json for serialization and deserialization """
import json

class FileStorage:
    """ Class stores a class object into a file so it can be used """
    __file_path = "json_data.json"
    __objects = {}

    # def __init__(self) -> None:

    def all(self):
      """ Return __objects"""
      return (FileStorage.__objects)
    
    def new(self, obj):
       FileStorage.__objects[obj.__class__.__name__.id] = obj

    def save(self):
       """ Serializes an object to file """
       with open(FileStorage.__file_path, mode="a+") as f:
          data = json.dumps(FileStorage.__objects)
          f.write(data)

    def reload(self):
      """ Deserializes an object back into the file storage """
      if(FileStorage.__file_path):
        with open(FileStorage.__file_path) as f:
            string = f.read()
            data = json.loads(string)
        FileStorage.__objects = data
      else:
          pass
      
      


