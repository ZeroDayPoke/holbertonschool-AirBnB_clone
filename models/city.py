#!/usr/bin/python3
"""Module for subclass: City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class 'City' that inherits from BaseModel"""
    state_id = ""
    name = ""
