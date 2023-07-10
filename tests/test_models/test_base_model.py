#!/usr/bin/python3

import sys
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    class for testing BaseModel class methods
    """
    def setUp(self):
        self.example = BaseModel()

    def test_BaseModel_attributes(self):
        self.assertTrue(isinstance(self.example.id, str))
        self.assertTrue(isinstance(self.example.created_at, datetime))
        self.assertTrue(isinstance(self.example.updated_at, datetime))
        self.assertTrue(isinstance(self.example.created_at, datetime))
        self.assertTrue(isinstance(self.example.updated_at, datetime))

    def test_BaseModel_todict(self):
        self.example_dict = self.example.to_dict()
        self.assertTrue(isinstance(self.example_dict, dict))
        self.assertTrue(len(self.example_dict.keys()) != 0)
        self.assertTrue(isinstance(datetime.strptime(self.example_dict\
                        ['created_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime))
        self.assertTrue(isinstance(datetime.strptime(self.example_dict\
                        ['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime))
