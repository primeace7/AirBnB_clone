#!/usr/bin/python3

'''
This module implements the base model class from which every
other class is created.
It defines all the fundamental features of all classes in this project.
'''
import uuid
import datetime

class BaseModel():
    '''
    Define the base model class

    Attributes:
    id(str): the unique identifier of an instance
    created_at(datetime): the date and time an instance is created
    updated_at(datetime): the date and time an instance is updated
    '''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime()
        self.updated_at = self.created_at

        def __str__(self):
            return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'
