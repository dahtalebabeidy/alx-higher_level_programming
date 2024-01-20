#!/usr/bin/python3
"""load_from_json_file"""

import json


def load_from_json_file(filename):
    """load_from_json_file"""
    with open(filename, 'r', encoding='utf-8') as file:
        python_obj = json.load(file)
