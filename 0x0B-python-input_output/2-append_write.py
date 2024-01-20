#!/usr/bin/python3
"""module for append_write function"""


def append_write(filename="", text=""):
    """writes text in filename"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
