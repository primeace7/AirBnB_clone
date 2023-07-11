#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    """
    Filestorage class for serializing and deserializing objects
    into and from files
    """
    __file_path = 'file.json'
    __objects = dict()

    def __int__(self):
        """
        init method for filestorage class
        """
        pass

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects
