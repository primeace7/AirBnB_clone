#!/usr/bin/python3

from models import storage
import unittest
from datetime import datetime
import uuid
from models.state import State

class TestState(unittest.TestCase):
    """
    class for testing State class methods
    """
    def setUp(self):
        self.example = State()

    def test_State_attributes(self):
        self.assertTrue(isinstance(self.example.id, str))
        self.assertTrue(isinstance(self.example.created_at, datetime))
        self.assertTrue(isinstance(self.example.updated_at, datetime))
        self.assertTrue(isinstance(self.example.created_at, datetime))
        self.assertTrue(isinstance(self.example.updated_at, datetime))
        self.assertEqual(self.example.created_at, self.example.updated_at)
        self.example.save()
        self.assertTrue(self.example.updated_at > self.example.created_at)

    def test_State_todict(self):
        self.example_dict = self.example.to_dict()
        self.assertTrue(isinstance(self.example_dict, dict))
        self.assertTrue(len(self.example_dict.keys()) != 0)
        self.assertTrue(isinstance(datetime.strptime(self.example_dict\
                        ['created_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime))
        self.assertTrue(isinstance(datetime.strptime(self.example_dict\
                        ['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime))
        self.assertEqual(self.example_dict['__class__'], type(self.example)\
                         .__name__)

    def test_State_fromdict(self):
        self.dict1 = self.example.to_dict()
        self.example2 = State(**self.dict1)

        for key in self.example2.__dict__.keys():
            self.assertTrue(key in self.example.__dict__.keys())
        self.assertEqual(type(self.example), type(self.example2))
        self.assertEqual(self.dict1['__class__'], type(self.example2).__name__)

    def test_State_storage_engine(self):
        self.example.save()
        storage.reload()
        stored_objects = storage.all()
        example_object_key = f'{type(self.example).__name__}.{self.example.id}'
        self.assertTrue(example_object_key in stored_objects.keys())
