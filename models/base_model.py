#!/usr/bin/python3
"""
This module contains the `BaseModel` class
for the Airbnb clone project
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel represents the base model of all the data models"""
    def __init__(self, *args, **kwargs):
        """
        Instantiation of the class `BaseModel` objects.

        Args:
            *args(tuple): Variable positioal arguments (unused).
            **kwargs(dict): The dictionary representation
            of an instance.
        """
        date_f = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs and len(kwargs) != 0:
            for key in kwargs:
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key], date_f)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key, date_f])
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Informal string representation of the class instance.

        Returns:
            str: string representation
         """
        return '[{}] ({}) \
                {}'.format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Retrieves a dictionary  representing a `BaseModel` instance.

        Returns:
            dict: a dictionary representation of a `BaseModel` instance.
        """
        dict_r = self.__dict__.copy()
        dict_r["__class__"] = type(self).__name__
        dict_r["created_at"] = self.created_at.isoformat()
        dict_r["updated_at"] = self.updated_at.isoformat()

        return dict_r

    def save(self):
        """
        Saves and updates the updated_at attribute
        with the current time.
        """
        self.updated_at = datetime.now()
        storage.save()
