#!/usr/bin/python3
"""module for student class"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return __dict__"""
        return self.__dict__
