#!/usr/bin/python3


"""This module contains the `User` class for the Airbnb clone project"""

from models.base_model.py import BaseModel


class User:
    """User represents the user attributes (public)  of all the data models"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
