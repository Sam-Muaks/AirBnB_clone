#!/usr/bin/python3
""" Init file
    Create an object from FileStorage Class
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
