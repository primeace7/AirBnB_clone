#!/usr/bin/python3

'''
This module implements the base model class from which every
other class is created.
It defines all the fundamental features of all classes in this project.
'''

import uuid
from datetime import datetime
import models

class BaseModel:
    '''
    Define the base model class

    Args:
    '''
    
    def save(self):
        """
        The public instance attribute updated_at has
        been updated with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        The fuction returns a dictionary that contains all the keys
        and values from __dict__ attribute of instance

        Return:
        dictionary(dict): A dictionary object
        that includes the contents of __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
