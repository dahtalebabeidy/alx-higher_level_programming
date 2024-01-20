#!/usr/bin/python3
"""module for read_file function"""


def read_file(filename=""):
    """reads filename"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
