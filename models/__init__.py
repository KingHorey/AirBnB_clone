#!/usr/bin/python3

""" Import file_storage for objects to v=be saved """
from models.engine import file_storage as file

storage = file.FileStorage()
storage.reload()
