#!/usr/bin/python3
""" Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class"""
    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""
