#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

type_stor = getenv("HBNB_TYPE_STORAGE")
if type_stor == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
