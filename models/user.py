#!/usr/bin/python3
"""This module contains the `User` class for the Airbnb clone project"""
from models.base_model import BaseModel


class User(BaseModel):
    """User represents the user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
