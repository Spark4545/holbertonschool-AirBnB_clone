#!/usr/bin/python3
"""
Contains FileStorage class
"""


import json
from models.base_model import BaseModel

classes = {"Basemodel": BaseModel}


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes them back to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with
        key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file path
        """
        jsonObject = {}
        for key in self.__objects:
            jsonObject[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(jsonObject, f)

    def relaod(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as f:
                jl = json.load()
            for key in jl:
                self.__objects[key] = classes[jl[key]["__class__"]](**jl[key])
        except FileNotFoundError:
            pass