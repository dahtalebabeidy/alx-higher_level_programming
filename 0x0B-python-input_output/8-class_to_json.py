#!/usr/bin/python3
"""module for def class_to_json"""


def class_to_json(obj):
    """returns dict"""
    return obj.__dict__
