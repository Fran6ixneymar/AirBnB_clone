#!/usr/bin/python3
"""This is the unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """This test Cases for the State class."""

    def setUp(self):
        """This sets up the test methods."""
        pass

    def tearDown(self):
        """This tears down the test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """This resets the FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """This tests the instantiation of State class."""

        b = State()
        self.assertEqual(str(type(b)), "<class 'models.state.State'>")
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """This tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        o = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
