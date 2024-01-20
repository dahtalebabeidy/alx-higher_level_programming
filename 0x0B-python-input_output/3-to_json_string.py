#!/usr/bin/python3
"""module for to_json_string"""

import json
"""import json module"""

def to_json_string(my_obj):
    """return my_obj json string"""
    return json.dumps(my_obj)
