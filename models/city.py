#!/usr/bin/python3
"""
This module contains the `City` class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the city"""
    state_id = ""
    name = ""
