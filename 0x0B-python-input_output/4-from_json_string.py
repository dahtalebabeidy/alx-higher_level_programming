#!/usr/bin/python3
"""from_json_string"""

import json


def from_json_string(my_str):
    """return my_str python object"""
    return json.loads(my_str)
