#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

"""This module contains the `BaseModel` class for the Airbnb clone project”””


class BaseModel:
	"""BaseModel represents the base model of all the data models”””


	def __init__(self):
    	“”” 
        Instantition of the class `BaseModel` objects.
        Args:
	id(uuid object): id of the model instance.
	created_at(datetime obj): The current datetime when an instance is created.
	updated _at(datetime obj): The current datetime when an instance is updated.
        “””
#if type(id) is not str:
#	raise TypeError (“id must be a string”)
#if not isinstance(created_at, datetime):
#	raise TypeError(“created_at must be a datetime instance”)
#If  not isinstance(updated_at, datetime):
#	raise TypeError(“updated_at must be a datetime instance”)
self.id = str(uuid4())
self.created_at = datetime.now()
self.update_at = datetime.now()

def __str__(self):
	“””
	Informal string representation of the class instance.
	
	Returns:
		str: string representation
”””
Return (‘[{}] ({}) {}’.format(type(self).__name__, self.id, self.__dict__))

def to_dict(self):
“””
Retrieves a dictionary  representing a `BaseModel` instance.
Returns:
	dict: a dictionary representation of a `BaseModel` instance.
“””
dict_r = self.__dict__.copy()
dict_r[“__class__”] =  type(self).__name__
dict_r[“created_at”] = self.created_at.isoformat()
dict_r[“updated_at”] = self.updated_at.isoformat()

return dict_r

def save(self):
	“””
	Saves and updates the updated_at attribute
	with the current time.
”””
self.updated_at = datetime.now()

