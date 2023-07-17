#!/usr/bin/python3
"""This is the base model script"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        '''String representation of this class instance'''
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Returns a timestamp on changes made to an instance'''
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary representation of this object instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """Recreates an object from a dictionary"""
        if '__class__' in obj_dict:
            class_name = obj_dict.pop('__class__')
            if class_name == cls.__name__:
                return cls(**obj_dict)
        return None
