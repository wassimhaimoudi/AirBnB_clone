#!/usr/bin/python3
"""This module defines the `FileStorage` class that will be used for storage"""
import json


class FileStorage:
    """Represents the storage system using json files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets a new object by its <class name>.id in the __object.
        Args:
            obj(obj): A BaseModel object
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves objects to to the JSON file"""
        try:
            obj_d = {}
            for key, val in FileStorage.__objects.items():
                obj_d[key] = val.to_dict()
            with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
                json.dump(obj_d, f)
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of the class name
        (each time a class is created you need to update this)"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }
        return classes

    def reload(self):
        """Reloads a JSON string dictionary from JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                from_json = json.load(f)
                FileStorage.__objects = {
                        key: self.classes()[val["__class__"]](**val)
                        for key, val in from_json.items()
                        }
        except FileNotFoundError:
            pass
