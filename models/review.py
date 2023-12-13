#!/usr/bin/python3
"""
This module contains the `Review` class
"""
from base_model import BaseModel


class Review(BaseModel):
    """Represents customer reviews"""

    place_id = ""
    user_id = ""
    text = ""
