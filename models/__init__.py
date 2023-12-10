#!/usr/bin/python3

"""This is the __init__ magic file"""

from models.engine import file_storage

storage = FileStorage()
storage.reload()
