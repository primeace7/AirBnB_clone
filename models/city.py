#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """
    Represents a city within a state

    Public class attributes:
    state_id: empty string
    name: empty string
    """
    name = ""
    state_id = ""
