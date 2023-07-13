#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    Represent a user

    Public class attributes:
    email: empty string
    password: empty string
    first_name: empty string
    last_name: empty string
    """
    email: ""
    password: ""
    first_name: ""
    last_name: ""
